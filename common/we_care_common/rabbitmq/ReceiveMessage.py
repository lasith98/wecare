from abc import ABC, abstractmethod

import pika

from we_care_common.rabbitmq.constant.Common import RABBITMQ_URL


class ReceiveMessage(ABC):
    def __init__(self, topic):
        self.__connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        self.__channel = None
        self.__topic = topic
        self.__channel = self.__connection.channel()
        self.__channel.queue_declare(self.__topic)
        self.__channel.basic_consume(queue=self.__topic, on_message_callback=self.message, auto_ack=True)

    @abstractmethod
    def message(self, method, channel, properties, body): pass

    def start_consuming(self):
        self.__channel.start_consuming()
        return self

    def close(self):
        self.__channel.close()
        self.__connection.close()
