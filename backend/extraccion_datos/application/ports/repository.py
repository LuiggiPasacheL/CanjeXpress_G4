
from abc import ABC, abstractmethod

from domain.file import File

class Repository(ABC):

    @abstractmethod
    def bulkInsertFile(self, file: File):
        pass
