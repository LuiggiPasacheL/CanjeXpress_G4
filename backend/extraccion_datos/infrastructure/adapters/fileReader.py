
from io import TextIOWrapper
from extraccion_datos.application.ports.reader import Reader


class FileReader(Reader):

    def __init__(self, encoding: str = "utf-8"):
        self.encoding = encoding

    def read(self, path: str) -> TextIOWrapper | None:
        if not path.endswith(".csv"):
            return None
        try:
            with open(path, "r", encoding=self.encoding) as file:
                return file

        except FileNotFoundError:
            return None
        
