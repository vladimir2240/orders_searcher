from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
from statistics import median as s_median
import time
import json
from communication import Logger

logger = Logger.get_logger('Websocket')


class BinanceWsWorkers:
    def __init__(self, volume_multiplicator):
        self.volume_multiplicator = volume_multiplicator

    def check_order_size(self, bids_asks:dict) -> list:
        '''
        :param bids_asks: dict {bids:[bids orders], asks:[ask orders]}
        :return: [{action: str(bids), volume: float(23.0), price:float(2.0)}, {}...]
        '''
        huge_orders = list()
        for action, orders in bids_asks.items():
            # Creates dict {volume:price,...}
            volumes_price_pairs = {float(order[1]): float(order[0]) for order in orders}
            volume_median = s_median(list(volumes_price_pairs.keys()))
            volume_sorted = sorted(list(volumes_price_pairs.keys()), reverse= True)
            for volume in volume_sorted:
                # if volume * self.volume_multiplicator > volume_median:
                if volume_median * self.volume_multiplicator < volume:
                    result_line = {
                        'action': action,
                        'volume': volume,
                        'price': volumes_price_pairs[volume]
                    }

                    huge_orders.append(result_line)
                else:
                    # If order lower, we don't need to continue iterating through sorted list
                    break
        return huge_orders


    def check_notification(self, last_data_from_buffer) -> dict:
        '''
        :param last_data_from_buffer:  Last buffer that needs to be checked
        :return: Dict of notifications { ticker: [{action: str(bids),
        volume: float(23.0), price:float(2.0)}, ... ]}
        '''
        stream_data = json.loads(last_data_from_buffer)
        ticker = stream_data.get('stream', None)
        if ticker:
            bids = stream_data['data']['bids']
            asks = stream_data['data']['asks']
            huge_orders = self.check_order_size(bids_asks={'bids': bids, 'asks': asks})
            if huge_orders:
                return {ticker: huge_orders}
        return dict()


    def websocket_controller(self, whitelist_tickers: list):
        '''
        Creating streams and searching orders that > 1000 times than median in last 40 orders(20 bids, 20 asks)
        '''
        binance_ws_manager = BinanceWebSocketApiManager(exchange="binance.com")
        # Cutting according to the limit of streams that available to open by default
        whitelist_tickers = whitelist_tickers[:1024]
        binance_ws_manager.create_stream(channels=['depth20'],
                                         markets=[ticker.lower() for ticker in whitelist_tickers])
        while True:
            if binance_ws_manager.is_manager_stopping():
                exit(0)
            last_data_from_buffer = binance_ws_manager.pop_stream_data_from_stream_buffer()
            if last_data_from_buffer is False:
                time.sleep(0.01)
            else:
                huge_orders = self.check_notification(last_data_from_buffer)
                if huge_orders:
                    # TODO: From here, you can continue working with data.
                    logger.info(huge_orders)
