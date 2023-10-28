import psycopg2
import os
from application.ports.product_query_repository import ProductQueryRepository
from domain.product import Product

class PostgresProductQueryRepository(ProductQueryRepository):
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
