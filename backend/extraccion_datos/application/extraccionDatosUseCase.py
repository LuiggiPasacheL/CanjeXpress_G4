
from extraccion_datos.application.ports.dataExtractor import DataExtractor
from extraccion_datos.application.ports.reader import Reader
from extraccion_datos.application.ports.repository import Repository

class ExtraccionDatosUseCase:
    def extraerDatos(self, dataExtractor: DataExtractor, reader: Reader, repository: Repository):
        try:
            file_paths : list[str] = dataExtractor.getFiles()
            if len(file_paths) == 0:
                return False
            for path in file_paths:
                data = reader.read(path)
                repository.bulkInsertData(data)
            return True
        except Exception as e:
            print(e)
            return False
