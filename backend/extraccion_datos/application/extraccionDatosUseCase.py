
import logging

from application.ports.dataExtractor import DataExtractor
from application.ports.repository import Repository
from domain.file import File

class ExtraccionDatosUseCase:
    def extraerDatos(self, dataExtractor: DataExtractor, repository: Repository):
        try:
            files : list[File] = dataExtractor.getFiles()
            for file in files:
                repository.bulkInsertFile(file)
        except Exception as e:
            logging.error(f"Error al extraer datos {e.__class__.__name__}")
