
from io import TextIOWrapper
from application.ports.repository import Repository

import psycopg2
import os

class PostgresRepository(Repository):

    def __init__(self, table_name: str):
        self.connection = psycopg2.connect(
            host=os.getenv("DATABASE_HOST", "localhost"),
            database=os.getenv("DATABASE_DB", "postgres"),
            user=os.getenv("DATABASE_USER", "postgres"),
            password=os.getenv("DATABASE_PASSWORD", "postgres")
        )

        self.query = f"COPY {table_name} FROM %s CSV HEADER"


    def bulkInsertData(self, data: TextIOWrapper):
        """ Insert list data into database """
        cursor = self.connection.cursor()

        try:
            cursor.execute(self.query, (data.name,))
            self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.rollback()

        cursor.close()
        self.connection.close()
