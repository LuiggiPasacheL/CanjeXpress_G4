
from abc import ABC, abstractmethod

class DataExtractor(ABC):

    @abstractmethod
    def getFiles(self) -> list[str]:
        pass
