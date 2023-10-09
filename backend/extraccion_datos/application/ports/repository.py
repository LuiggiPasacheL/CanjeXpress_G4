
from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def BulkInsert(self, data):
        pass
