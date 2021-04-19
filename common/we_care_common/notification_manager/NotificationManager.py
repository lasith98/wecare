from singleton_decorator import singleton

from we_care_common.notification_manager.ManagerFactory import ManagerFactory
from we_care_common.notification_manager.MessageModel import MessageModel
from we_care_common.notification_manager.enumeration.ManagerType import ManagerType


@singleton
class NotificationManager(object):
    def send(self, type: ManagerType, model: MessageModel):
        ManagerFactory.get_manger(type).send(model)
