import psycopg2
import os
import logging

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
        query = "SELECT id, username, password, points, profile_picture, is_admin FROM users WHERE username = %s"
        cur.execute(query, (username,))
        r = cur.fetchone()
        cur.close()
        if r:
            return User(r[0], r[1], r[2], r[3], r[4], r[5])
        else:
            return None

    def update_user_points(self, user_id: int, points: int) -> None:
        cur = self.conn.cursor()
        query = "UPDATE users SET points = %s WHERE id = %s"
        cur.execute(query, (points, user_id))
        self.conn.commit()
        cur.close()

    def update_product_user(self, user_id: int, product_id: int, required_quantity: int) -> None:
        print(f'Updating {required_quantity} product {product_id} for user {user_id}')

    def get_user_by_id(self, id: int) -> User | None:
        cur = self.conn.cursor()
        query = "SELECT id, username, password, points, profile_picture, is_admin FROM users WHERE id = %s"
        cur.execute(query, (id,))
        r = cur.fetchone()
        cur.close()
        if r:
            return User(r[0], r[1], r[2], r[3], r[4], r[5])
        else:
            return None

    def bulk_create_users(self, users_data: list[dict]) -> None:
        query = """
                    INSERT INTO users (username, password, points, profile_picture, is_admin)
                    VALUES (%(username)s, %(password)s, %(points)s, %(profile_picture)s, %(is_admin)s)
                """
        cur = self.conn.cursor()
        try:
            cur.executemany(query, users_data)
            self.conn.commit()
            logging.info(f"Usuarios insertados exitosamente.")
        except Exception as e:
            self.conn.rollback()
            logging.error(f"Error al insertar datos: {e}")
