
import logging

from dataclasses import dataclass
from io import TextIOWrapper

@dataclass
class File:
    path: str

    def __init__(self, path: str):
        self.path = path

    def read(self, encoding: str = "utf-8") -> TextIOWrapper | None:
        if not self.path.endswith(".csv"):
            logging.info("File must be a .csv file")
            return None
        try:
            with open(self.path, "r", encoding=encoding) as file:
                return file
        except Exception as e:
            print(e)
            return None
