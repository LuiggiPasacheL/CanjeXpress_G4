
from abc import ABC, abstractmethod

class Reader(ABC):
    """
    Abstract class for reading data from a source.
    """

    @abstractmethod
    def Read(self):
        pass
