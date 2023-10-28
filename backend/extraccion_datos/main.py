
import os
import time
import logging

from application.extraccionDatosUseCase import ExtraccionDatosUseCase
from infrastructure.adapters.fileExtractor import FileExtractor
from infrastructure.adapters.mockRepository import MockRepository

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("logs.log"),
        logging.StreamHandler()
    ]
)

def main():
    directory = os.path.join(os.path.dirname(__file__), "data")

    dataExtractor = FileExtractor(directory)
    repository = MockRepository(table_name=os.getenv("TABLE_NAME", "data"))

    extraccionDatosUseCase = ExtraccionDatosUseCase()

    logging.info("Iniciando extracción de datos")

    while True:
        extraccionDatosUseCase.extraerDatos(dataExtractor, repository)
        time.sleep(5)

if __name__ == "__main__":
    main()
