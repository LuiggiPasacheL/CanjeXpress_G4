
import os

class PostgreSQLService:

    def __init__(self) -> None:
        self.__host = os.environ.get('POSTGRESQL_HOST')
        self.__port = os.environ.get('POSTGRESQL_PORT')
        self.__user = os.environ.get('POSTGRESQL_USER')
        self.__password = os.environ.get('POSTGRESQL_PASSWORD')
        self.__database = os.environ.get('POSTGRESQL_DATABASE')

