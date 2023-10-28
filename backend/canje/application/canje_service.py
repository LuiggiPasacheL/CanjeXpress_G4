from application.ports.product_repository import ProductRepository
from application.ports.user_repository import UserRepository
import logging

logging.basicConfig(level=logging.INFO)
class CanjeService:
    def __init__(self, user_repository: UserRepository, product_repository: ProductRepository):
        self.user_repository = user_repository
        self.product_repository = product_repository

    def canjear(self, user_id: int, cart: list) -> dict:
        total_points_needed = 0
        insufficient_stock_products = []
        not_found_products = []

        user_exists = self.user_repository.user_exists(user_id)
        if not user_exists:
            return {"success": False, "message": "USER_NOT_FOUND"}

        for item in cart:
            product = self.product_repository.get_product_by_id(item['product_id'])
            if not product:
                not_found_products.append(item['product_id'])
                continue
            if product.quantity < item['quantity']:
                insufficient_stock_products.append(item['product_id'])
            total_points_needed += product.points * item['quantity']

        if not_found_products:
            return {"success": False, "message": "PRODUCT_NOT_FOUND", "products": not_found_products}

        if insufficient_stock_products:
            return {"success": False, "message": "INSUFFICIENT_STOCK", "products": insufficient_stock_products}

        user_points = self.user_repository.get_user_points(user_id)
        if user_points < total_points_needed:
            logging.info(f"USER POINTS: {user_points}")
            logging.info(f"TOTAL POINTS: {total_points_needed}")
            return {"success": False, "message": "INSUFFICIENT_POINTS"}

        for item in cart:
            self.product_repository.deduct_product_quantity(item['product_id'], item['quantity'])

        self.user_repository.deduct_points(user_id, total_points_needed)

        self.product_repository.register_exchange(user_id, cart, total_points_needed)

        return {"success": True, "message": "CANJE_SUCCESSFUL"}