
class ProductNotFound(Exception):
    def __init__(self, product_id: int ):
        super().__init__(f"Product with id {product_id} not found")
