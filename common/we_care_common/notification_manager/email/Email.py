from we_care_common.notification_manager.MessageModel import MessageModel


class Email(MessageModel):
    email = ""

    def to_dict(self):
        return self.__dict__
