from abc import ABC, abstractmethod


class Api(ABC):
    @abstractmethod
    def find_all(self): pass

    @abstractmethod
    def find_by_id(self, id): pass

    @abstractmethod
    def search(self, query): pass
