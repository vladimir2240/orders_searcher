#!/usr/bin/env python
from modules.config import init_config
from modules.services import BinanceHandler
from modules.controllers import BinanceOrderController
from communication.kafka import ActionsProducer
from communication.logging import Logger


logger = Logger.get_logger('Binance Order Scanner')

if __name__ == "__main__":
    logger.info('Starting the program...')
    binance_order_controller = BinanceOrderController(binance_handler=BinanceHandler(), config = init_config(),
                                                      kafka_producer=ActionsProducer)
    binance_order_controller.binance_orderbook_scrapper()
