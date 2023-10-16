
from io import TextIOWrapper
from application.ports.reader import Reader


class FileReader(Reader):

    def __init__(self, encoding: str = "utf-8"):
        self.encoding = encoding

    def read(self, path: str) -> TextIOWrapper | None:
        if not path.endswith(".csv"):
            print("File must be a .csv file")
            return None
        try:
            with open(path, "r", encoding=self.encoding) as file:
                return file

        except FileNotFoundError:
            print("File not found")
            return None
        
