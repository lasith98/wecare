from we_care_common.notification_manager.Manager import Manager
from we_care_common.notification_manager.email.EmailManager import EmailManager
from we_care_common.notification_manager.enumeration.ManagerType import ManagerType
from we_care_common.notification_manager.sms.SMSManager import SMSManager


class ManagerFactory:
    @staticmethod
    def get_manger(type: ManagerType) -> Manager:
        if ManagerType.EMAIL == type:
            return EmailManager()
        elif ManagerType.SMS == type:
            return SMSManager()
