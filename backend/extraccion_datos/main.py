
import os

from os import path
from extraccion_datos.application.extraccionDatosUseCase import ExtraccionDatosUseCase

from extraccion_datos.infrastructure.adapters.fileExtractor import FileExtractor
from extraccion_datos.infrastructure.adapters.fileReader import FileReader
from extraccion_datos.infrastructure.adapters.postgresRepository import PostgresRepository


def main():

    dataExtractor = FileExtractor(path.join(path.dirname(__file__), "..", "data"))
    reader = FileReader(encoding="utf-8")
    repository = PostgresRepository(table_name=os.getenv("TABLE_NAME", "data"))

    extraccionDatosUseCase = ExtraccionDatosUseCase()
    ok : bool = extraccionDatosUseCase.extraerDatos(dataExtractor, reader, repository)

    if ok:
        print("Datos extraidos correctamente")
