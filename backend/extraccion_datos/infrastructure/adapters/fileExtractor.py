
import os
from application.ports.dataExtractor import DataExtractor
from domain.file import File

class FileExtractor(DataExtractor):
    
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
        self.registry = set()
    
    def getFiles(self) -> list[File]:
        listdir = os.listdir(self.dir_path)
        files = []
        for i in range(len(listdir)):
            listdir[i] = self.dir_path + '/' + listdir[i]
            if listdir[i] not in self.registry:
                files.append(File(listdir[i]))
                self.registry.add(listdir[i])
        return files
