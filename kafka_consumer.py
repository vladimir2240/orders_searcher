'''
Just the example how consumer may work
'''
import time
from communication.logging import Logger
from communication.kafka import ActionsConsumer


logger = Logger.get_logger('Kafka Consumer')
consumer = ActionsConsumer(topic='huge_order')
logger.info('Consumer is ON')

for order in consumer.read_action():
    logger.info(order)