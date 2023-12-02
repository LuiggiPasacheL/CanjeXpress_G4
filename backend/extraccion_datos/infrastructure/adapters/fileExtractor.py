import os
import ftplib

from application.ports.dataExtractor import DataExtractor
from domain.file import File

class FileExtractor(DataExtractor):
    
    # Define las credenciales y la ruta del servidor FTP directamente en la clase
    FTP_SERVER = 'ftpupload.net'
    FTP_USER = 'b5_35544545'
    FTP_PASSWORD = '6714db43f7'
    FTP_PATH = '/etl'  # Asegúrate de cambiar esto por la ruta correcta en tu servidor FTP
    LOCAL_DIR_PATH = 'data'  # Ruta local para guardar los archivos descargados

    def __init__(self):
        self.dir_path = FileExtractor.LOCAL_DIR_PATH
        self.registry = set()
        # Asegúrate de que existe el directorio local 'data'
        os.makedirs(self.dir_path, exist_ok=True)
    
    def connect_ftp(self):
        # Establecer conexión FTP
        self.ftp = ftplib.FTP(FileExtractor.FTP_SERVER)
        self.ftp.login(FileExtractor.FTP_USER, FileExtractor.FTP_PASSWORD)
        self.ftp.cwd(FileExtractor.FTP_PATH)

    def disconnect_ftp(self):
        self.ftp.quit()
    def download_csv_files(self):
        # Conectar al servidor FTP
        self.connect_ftp()
        # Listar archivos en el directorio FTP y filtrar por .csv
        files = self.ftp.nlst()
        csv_files = [file for file in files if file.lower().endswith('.csv')]
        # Descargar los archivos .csv
        for filename in csv_files:
            local_filename = os.path.join(self.dir_path, filename)
            print("DESCARGANDO :",local_filename)
            with open(local_filename, 'wb') as local_file:
                self.ftp.retrbinary('RETR ' + filename, local_file.write)
        # Desconectar del servidor FTP
        self.disconnect_ftp()
    
    def getFiles(self) -> list[File]:
        # Descargar archivos .csv del servidor FTP
        self.download_csv_files()
        # Listar archivos en el directorio local 'data'
        listdir = os.listdir(self.dir_path)
        files = []
        for filename in listdir:
            filepath = os.path.join(self.dir_path, filename)
            if filepath not in self.registry:
                files.append(File(filepath))
                self.registry.add(filepath)
        return files
