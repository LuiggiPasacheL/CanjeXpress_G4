
from abc import ABC, abstractmethod

class DataExtractor(ABC):

    @abstractmethod
    def Extract(self):
        pass
