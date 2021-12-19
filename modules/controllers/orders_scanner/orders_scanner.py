from modules.services.binance_websocket import BinanceWsWorkers
from communication import Logger

logger = Logger.get_logger('Controller')

class BinanceOrderController:
    def __init__(self, binance_handler, config):
        self._binance_handler = binance_handler
        self._config = config

    def binance_scanner(self):
        logger.info('Started preparing whitelist tickers')
        # Define whitelist tickers, which will be used to create WS streams
        whitelist_tickers = self._binance_handler.define_pairs(quotes=self._config.get('quotes'),
                                                             exact_pairs=self._config.get('exact_pairs'))

        logger.info(f'Preparation finished. You selected {len(whitelist_tickers)} pairs. Creating streams...')
        binance_ws = BinanceWsWorkers(volume_multiplicator=self._config.get('volume_multiplicator'))
        # Start WS connection
        try:
            binance_ws.websocket_controller(whitelist_tickers=whitelist_tickers)
        except Exception as error:
            logger.error(f'While working error occurs:  {error}\n Let`s try again...')