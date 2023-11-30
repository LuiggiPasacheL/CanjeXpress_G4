
class InsufficientPoints(Exception):
    def __init__(self):
        self.message = "the user has not enough points to buy all products"

class ProductNotFound(Exception):
    def __init__(self, product_id: int):
        self.message = f"the product {product_id} was not found"

class InsufficientStock(Exception):
    def __init__(self, product_id: int):
        self.message = f"the product {product_id} has not enough stock to buy all products"
