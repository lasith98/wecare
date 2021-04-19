from we_care_common.notification_manager.MessageModel import MessageModel


class SMS(MessageModel):
    message = ''
    phone = ''

    def to_dict(self):
        return self.__dict__
