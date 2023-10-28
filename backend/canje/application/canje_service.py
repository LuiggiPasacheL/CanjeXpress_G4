from application.ports.product_query_repository import ProductQueryRepository
from application.ports.product_command_repository import ProductCommandRepository
from application.ports.user_query_repository import UserQueryRepository
from application.ports.user_command_repository import UserCommandRepository
from infrastructure.adapters.rabbitmq_producer import publish_message

import logging

logging.basicConfig(level=logging.INFO)

class CanjeService:
    def __init__(self, 
                 user_query_repository: UserQueryRepository, 
                 user_command_repository: UserCommandRepository, 
                 product_query_repository: ProductQueryRepository, 
                 product_command_repository: ProductCommandRepository):
        self.user_query_repository = user_query_repository
        self.user_command_repository = user_command_repository
        self.product_query_repository = product_query_repository
        self.product_command_repository = product_command_repository

    def canjear(self, user_id: int, cart: list) -> dict:
        total_points_needed = 0
        insufficient_stock_products = []
        not_found_products = []

        user_exists = self.user_query_repository.user_exists(user_id)
        if not user_exists:
            publish_message('canje_queue', 'Error al procesar canje : USER_NOT_FOUND')
            return {"success": False, "message": "USER_NOT_FOUND"}

        for item in cart:
            product = self.product_query_repository.get_product_by_id(item['product_id'])
            if not product:
                not_found_products.append(item['product_id'])
                continue
            if product.quantity < item['quantity']:
                insufficient_stock_products.append(item['product_id'])
            total_points_needed += product.points * item['quantity']

        if not_found_products:
            publish_message('canje_queue', f'''PRODUCT_NOT_FOUND: {not_found_products}''', )
            return {"success": False, "message": "PRODUCT_NOT_FOUND", "products": not_found_products}

        if insufficient_stock_products:
            publish_message('canje_queue', f'''INSUFFICIENT_STOCK: {insufficient_stock_products}''', )
            return {"success": False, "message": "INSUFFICIENT_STOCK", "products": insufficient_stock_products}

        user_points = self.user_query_repository.get_user_points(user_id)
        if user_points < total_points_needed:
            logging.info(f"USER POINTS: {user_points}")
            logging.info(f"TOTAL POINTS: {total_points_needed}")
            publish_message('canje_queue', f'''INSUFFICIENT_POINTS: \nUSER POINTS: {user_points} \n TOTAL POINTS: {total_points_needed}''', )

            return {"success": False, "message": "INSUFFICIENT_POINTS"}

        for item in cart:
            self.product_command_repository.deduct_product_quantity(item['product_id'], item['quantity'])

        self.user_command_repository.deduct_points(user_id, total_points_needed)

        self.product_command_repository.register_exchange(user_id, cart, total_points_needed)
        publish_message('canje_queue', 'Canje procesado exitosamente')
        return {"success": True, "message": "CANJE_SUCCESSFUL"}
