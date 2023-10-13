
import os
from extraccion_datos.application.ports.dataExtractor import DataExtractor


class FileExtractor(DataExtractor):
    
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
    
    def getFiles(self) -> list[str]:
        return os.listdir(self.dir_path)
