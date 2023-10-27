
import os
import logging
import psycopg2

from application.ports.repository import Repository

from domain.file import File

class PostgresRepository(Repository):

    def __init__(self, table_name: str):
        self.connection = psycopg2.connect(
            host=os.getenv("DATABASE_HOST", "localhost"),
            database=os.getenv("DATABASE_DB", "postgres"),
            user=os.getenv("DATABASE_USER", "postgres"),
            password=os.getenv("DATABASE_PASSWORD", "postgres")
        )

        self.query = f"COPY {table_name} FROM %s CSV HEADER"


    def bulkInsertFile(self, file: File):
        """ Insert list data into database """
        cursor = self.connection.cursor()
        
        try:
            data = file.read()
            if data is not None:
                cursor.execute(self.query, (data.name,))
                self.connection.commit()
        except Exception as e:
            logging.error(f"Error while bulk insert data {e.__class__.__name__}")
            self.connection.rollback()

        cursor.close()
        self.connection.close()
