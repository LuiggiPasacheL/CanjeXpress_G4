
from extraccion_datos.application.ports.dataExtractor import DataExtractor
from extraccion_datos.application.ports.reader import Reader
from extraccion_datos.application.ports.repository import Repository

class ExtraccionDatosUseCase:
    def extraerDatos(self, dataExtractor: DataExtractor, reader: Reader, repository: Repository):
        try:
            file_path = dataExtractor.createFile()
            data = reader.read(file_path)
            repository.bulkInsertData(data)
            return True
        except Exception as e:
            print(e)
            return False
