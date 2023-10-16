
import os
from application.ports.dataExtractor import DataExtractor


class FileExtractor(DataExtractor):
    
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
    
    def getFiles(self) -> list[str]:
        listdir = os.listdir(self.dir_path)
        for i in range(len(listdir)):
            path = self.dir_path + '/'
            listdir[i] = path + listdir[i]
        return listdir
