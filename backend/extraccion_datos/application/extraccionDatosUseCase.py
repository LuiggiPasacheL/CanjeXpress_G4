
import logging
import csv

from application.ports.dataExtractor import DataExtractor
from application.ports.repository import Repository
from domain.file import File

class ExtraccionDatosUseCase:
    def __init__(self, dataExtractor: DataExtractor, repository: Repository):
        self.dataExtractor = dataExtractor
        self.repository = repository

    def execute(self) -> list[dict]|None:
        try:
            files : list[File] = self.dataExtractor.getFiles()
            users_data = []
            for file in files:
                users_data += self.get_users_data(file.path)
                self.repository.bulkInsertFile(file)
            return users_data
        except Exception as e:
            logging.error(f"Error al extraer datos: {e.__class__.__name__}")
            return None

    def get_users_data(self, file_path: str) -> list[dict]:
        users_data = []
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users_data.append(row)
        return users_data
