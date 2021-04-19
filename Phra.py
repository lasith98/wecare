import json

from we_care_common.rabbitmq.constant.TopicConstant import PRESCRIPTION

from we_care_common.rabbitmq.ReceiveMessage import ReceiveMessage


class Pha(ReceiveMessage):
    def message(self, method, channel, properties, body):
        print(json.loads(body))


Pha(PRESCRIPTION).start_consuming()
