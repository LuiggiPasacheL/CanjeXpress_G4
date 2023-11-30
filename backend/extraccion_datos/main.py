
import os
import time
import logging

from application.extraccionDatosUseCase import ExtraccionDatosUseCase
from application.requestCreateUserUseCase import RequestCreateUserUseCase
from infrastructure.adapters.fileExtractor import FileExtractor
from infrastructure.adapters.mockRepository import MockRepository
from infrastructure.adapters.rmqRequestCreateUser import RMQRequestCreateUser

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("logs.log"),
        logging.StreamHandler()
    ]
)
directory = os.path.join(os.path.dirname(__file__), "data")

dataExtractor = FileExtractor(directory)

repository = MockRepository(table_name=os.getenv("TABLE_NAME", "data"))
requestCreateUser = RMQRequestCreateUser()

requestCreateUserUseCase = RequestCreateUserUseCase(requestCreateUser)
extraccionDatosUseCase = ExtraccionDatosUseCase(dataExtractor, repository)

def main():
    logging.info("Iniciando extracción de datos")

    while True:
        users_data = extraccionDatosUseCase.execute()
        if users_data is not None and len(users_data) > 0:
            requestCreateUserUseCase.execute(users_data)
        time.sleep(5)

if __name__ == "__main__":
    time.sleep(5)
    main()
