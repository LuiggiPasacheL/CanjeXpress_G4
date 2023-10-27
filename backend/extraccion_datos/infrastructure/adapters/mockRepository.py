
import logging
from application.ports.repository import Repository
from domain.file import File

class MockRepository(Repository):

    def __init__(self, table_name: str):
        self.table_name = table_name
        self.processed_files = set()

    def bulkInsertFile(self, file: File):
        data = file.read()
        if data is not None:
            logging.info(f"Inserting data file {data.name} into {self.table_name} table")
