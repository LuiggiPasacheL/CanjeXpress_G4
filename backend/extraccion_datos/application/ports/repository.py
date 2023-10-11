
from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def bulkInsertData(self, data):
        pass
