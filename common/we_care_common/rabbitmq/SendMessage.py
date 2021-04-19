import json

import pika

from we_care_common.rabbitmq.constant.Common import RABBITMQ_URL
from we_care_common.rabbitmq.exception.MessageQueueException import MessageQueueException


class SendMessage(object):
    def __init__(self, topic):
        self.__connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        self.__channel = None
        self.__topic = topic

    def send(self, payload, properties=''):
        if isinstance(payload, dict):
            self.open()
            self.__channel.basic_publish('', routing_key=self.__topic, body=json.dumps(payload),
                                         properties=pika.BasicProperties(properties))
        else:
            raise MessageQueueException("Payload type is {0} but required dict type".format(type(payload)))

    def open(self):
        self.__channel = self.__connection.channel()
        return self

    def close(self):
        self.__channel.close()
        self.__connection.close()
