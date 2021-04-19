from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def send(self, model): pass
