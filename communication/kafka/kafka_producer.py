from kafka import KafkaProducer
from kafka import errors
from json import dumps
import os
import time
from communication.logging import Logger

logger = Logger.get_logger('Kafka Producer')

class ActionsProducer:
    '''
    Creates simple kafka producer
    '''
    def __init__(self, topic:str):
        self.topic = topic
        try:
            # Just waiting while kafka starting (example: First Start)
            time.sleep(10)
            self._producer = KafkaProducer(
                bootstrap_servers=[os.getenv('KAFKA_CONN')],
                value_serializer=lambda x: dumps(x).encode('utf-8')
            )

        except errors.NoBrokersAvailable as err:
            # Something wrong with connection to Kafka
            logger.error(err)


    def add_action(self, data):
        '''
        Sending new message (any data)
        '''
        self._producer.send(self.topic, value=data)
