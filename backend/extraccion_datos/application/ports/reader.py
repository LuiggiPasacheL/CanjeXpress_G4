
from abc import ABC, abstractmethod
from io import TextIOWrapper

class Reader(ABC):
    """
    Abstract class for reading data from a source.
    """

    @abstractmethod
    def read(self, file_path: str) -> TextIOWrapper | None:
        pass
