import json

from we_care_common.rabbitmq.constant.TopicConstant import LAB_REPORT

from we_care_common.rabbitmq.ReceiveMessage import ReceiveMessage


class Lab(ReceiveMessage):
    def message(self, method, channel, properties, body):
        print(json.loads(body))


Lab(LAB_REPORT).start_consuming()
