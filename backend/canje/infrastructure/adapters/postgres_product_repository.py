import psycopg2
import os

from application.ports.product_repository import ProductRepository
from domain.product import Product


class PostgresProductRepository(ProductRepository):
    def __init__(self):
        self.conn = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
        )

    def get_product_by_id(self, product_id: int) -> Product:
        cur = self.conn.cursor()
        query = "SELECT id, name, points, description, image_url, quantity FROM products WHERE id = %s"
        cur.execute(query, (product_id,))
        r = cur.fetchone()
        cur.close()
        if r:
            return Product(r[0], r[1], r[2], r[3], r[4], r[5])
        else:
            return None
    def deduct_product_quantity(self, product_id: int, quantity: int):
        cur = self.conn.cursor()
        query = "UPDATE products SET quantity = quantity - %s WHERE id = %s AND quantity >= %s"
        cur.execute(query, (quantity, product_id, quantity))
        affected_rows = cur.rowcount
        self.conn.commit()
        cur.close()
        return affected_rows > 0
    
    def register_exchange(self, user_id: int, cart: list, total_points: int):
        cur = self.conn.cursor()
        query = """
        INSERT INTO exchange_history (user_id, total_points) VALUES (%s, %s) RETURNING exchange_id;
        """
        cur.execute(query, (user_id, total_points))
        exchange_id = cur.fetchone()[0]

        for item in cart:
            detail_query = """
            INSERT INTO exchange_details (exchange_id, product_id, quantity) VALUES (%s, %s, %s);
            """
            cur.execute(detail_query, (exchange_id, item['product_id'], item['quantity']))

        self.conn.commit()
        cur.close()
