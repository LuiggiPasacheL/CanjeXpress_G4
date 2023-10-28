import psycopg2
import os
from application.ports.user_command_repository import UserCommandRepository

class PostgresUserCommandRepository(UserCommandRepository):
    def __init__(self):
        self.conn = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
        )

    def deduct_points(self, user_id: int, points: int):
        cur = self.conn.cursor()
        query = "UPDATE users SET points = points - %s WHERE id = %s"
        cur.execute(query, (points, user_id))
        self.conn.commit()
        cur.close()
