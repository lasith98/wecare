from we_care_common.notification_manager.Manager import Manager
from we_care_common.notification_manager.email.Email import Email


class EmailManager(Manager):
    def send(self, model: Email):
        print("Sending dummy email")
        print("Email : {}".format(model.email))
