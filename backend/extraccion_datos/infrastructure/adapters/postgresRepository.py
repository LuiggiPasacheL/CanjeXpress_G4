
from application.ports.repository import Repository

import psycopg2
import os

class PostgresRepository(Repository):

    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv("DATABASE_HOST", "localhost"),
            database=os.getenv("DATABASE_DB", "postgres"),
            user=os.getenv("DATABASE_USER", "postgres"),
            password=os.getenv("DATABASE_PASSWORD", "postgres")
        )

    def bulkInsertData(self, data: list):
        """ Insert list data into database """
        cursor = self.connection.cursor()
        cursor.executemany(
            "INSERT INTO users (name, email) VALUES (%s, %s)", data)
        self.connection.commit()
        cursor.close()
