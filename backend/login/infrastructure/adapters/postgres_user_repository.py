import psycopg2
import os

from application.ports.user_repository import UserRepository
from domain.user import User

class PostgresUserRepository(UserRepository):
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv('DATABASE_HOST'),
            port=os.getenv('DATABASE_PORT'),
            dbname=os.getenv('DATABASE_NAME'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD')
        )

    def get_user_by_username(self, username: str) -> User | None:
        cur = self.conn.cursor()
        query = "SELECT username, password FROM users WHERE username = %s"
        cur.execute(query, (username,))
        r = cur.fetchone()
        cur.close()
        if r:
            return User(r[0],r[1])
        else:
            return None
    
