from we_care_common.notification_manager.Manager import Manager
from we_care_common.notification_manager.sms.SMS import SMS


class SMSManager(Manager):

    def send(self, model: SMS):
        print("Sending  dummy sms ")
        print("To : {}".format(model.phone))
        print("message : {}".format(model.message))
