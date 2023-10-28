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
        query = "SELECT id, username, password, points FROM users WHERE username = %s"
        cur.execute(query, (username,))
        r = cur.fetchone()
        cur.close()
        if r:
            return User(r[0], r[1], r[2], r[3])
        else:
            return None

    def get_user_points(self, user_id: int) -> int:
        cur = self.conn.cursor()
        query = "SELECT points FROM users WHERE id = %s"
        cur.execute(query, (user_id,))
        r = cur.fetchone()
        cur.close()
        return r[0] if r else 0

    def deduct_points(self, user_id: int, points: int):
        cur = self.conn.cursor()
        query = "UPDATE users SET points = points - %s WHERE id = %s"
        cur.execute(query, (points, user_id))
        self.conn.commit()
        cur.close()


    def user_exists(self, user_id: int) -> bool:
        cur = self.conn.cursor()
        query = "SELECT id FROM users WHERE id = %s"
        cur.execute(query, (user_id,))
        r = cur.fetchone()
        cur.close()
        return r is not None        