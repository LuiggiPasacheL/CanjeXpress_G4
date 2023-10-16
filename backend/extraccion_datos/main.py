
import os

from os import path
from application.extraccionDatosUseCase import ExtraccionDatosUseCase

from infrastructure.adapters.fileExtractor import FileExtractor
from infrastructure.adapters.fileReader import FileReader
from infrastructure.adapters.mockRepository import MockRepository


def main():

    dataExtractor = FileExtractor(path.join(path.dirname(__file__), "data"))
    reader = FileReader(encoding="utf-8")
    repository = MockRepository(table_name=os.getenv("TABLE_NAME", "data"))

    extraccionDatosUseCase = ExtraccionDatosUseCase()
    ok : bool = extraccionDatosUseCase.extraerDatos(dataExtractor, reader, repository)

    if ok:
        print("Datos extraidos correctamente")

if __name__ == "__main__":
    main()
