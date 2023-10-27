
from abc import ABC, abstractmethod

from domain.file import File

class DataExtractor(ABC):

    @abstractmethod
    def getFiles(self) -> list[File]:
        pass
