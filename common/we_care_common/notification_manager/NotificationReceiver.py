import json

from we_care_common.rabbitmq.ReceiveMessage import ReceiveMessage


class NotificationReceiver(ReceiveMessage):
    def message(self, method, channel, properties, body):
        print(json.loads(body))
