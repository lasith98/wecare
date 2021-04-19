from abc import ABC, abstractmethod


class MessageModel(ABC):
    @abstractmethod
    def to_dict(self): pass
