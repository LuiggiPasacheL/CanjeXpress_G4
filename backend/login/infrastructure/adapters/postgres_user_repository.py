import psycopg2
import os

from application.ports.user_repository import UserRepository
from domain.user import User

class PostgresUserRepository(UserRepository):
    def __init__(self):
        self.conn = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
        )

    def get_user_by_username(self, username: str) -> User | None:
        cur = self.conn.cursor()
        query = "SELECT username, password FROM users WHERE username = %s" # user: user, password: password
        cur.execute(query, (username,))
        r = cur.fetchone()
        cur.close()
        if r:
            return User(r[0],r[1])
        else:
            return None
    
