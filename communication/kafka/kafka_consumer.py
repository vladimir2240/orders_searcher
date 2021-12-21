from kafka import KafkaConsumer
from json import loads
import os

class ActionsConsumer:
    '''
    Creates simple kafka consumer
    '''
    def __init__(self, topic:str):
        self._consumer = KafkaConsumer(
            topic,
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group-id',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )

    def read_action(self):
        '''
        Returns new messages from Kafka
        '''
        for event in self._consumer:
            print(event.value)