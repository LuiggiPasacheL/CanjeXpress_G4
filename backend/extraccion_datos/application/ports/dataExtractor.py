
from abc import ABC, abstractmethod

class DataExtractor(ABC):

    @abstractmethod
    def createFile(self) -> str:
        pass
