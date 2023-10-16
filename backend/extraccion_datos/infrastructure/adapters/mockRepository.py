
from io import TextIOWrapper
from application.ports.repository import Repository

class MockRepository(Repository):

    def __init__(self, table_name: str):
        self.table_name = table_name

    def bulkInsertData(self, data: TextIOWrapper):
        print(f"Inserting data file {data.name} into {self.table_name} table")
