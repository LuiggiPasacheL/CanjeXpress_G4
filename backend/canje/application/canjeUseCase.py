
import logging
from application.ports.productsRepository import ProductsRepository
from application.ports.userRepository import UserRepository
from domain.product import Product

from domain.user import User
from application.exceptions import InsufficientPoints, InsufficientStock

class CanjeUseCase:

    def __init__(self, productsRepository: ProductsRepository, userRepository: UserRepository):
        self.productsRepository = productsRepository
        self.userRepository = userRepository


    def canjear(self, user: User, cart: list):
        def validateUserPoints(user: User, products: list[Product]):
            """Validates if the user has enough points to buy all products in the cart"""
            user.points -= sum([product.points for product in products])
            if user.points < 0:
                raise InsufficientPoints()

        def validateProducts(products: list[Product]):
            """Validates if all products in the cart are in stock"""
            for product in products:
                if product.stock < 0 or product.stock - product.requiredQuantity < 0:
                    raise InsufficientStock(product.id)

        products = self.productsRepository.getProducts(cart)

        validateUserPoints(user, products)
        validateProducts(products)

        # TODO: If validations are ok, update user points and products stock
            # TODO: Update user points, Message in peka: UserId, reducedPoints, productsIds, productsRequiredQuantity
        self.userRepository.updateUser(user, products)
        logging.info(f'Usuario {user.id} con {user.points} puntos está canjeando estos productos {products}')
            # TODO: Update all products stock
        self.productsRepository.updateProducts(products)

