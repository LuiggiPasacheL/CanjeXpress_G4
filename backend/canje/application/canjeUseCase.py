
import logging
from application.ports.productsRepository import ProductsRepository

from domain.user import User


class CanjeUseCase:

    def __init__(self, productsRepository: ProductsRepository):
        self.productsRepository = productsRepository

    def canjear(self, user: User, cart: list):
        products = self.productsRepository.getProducts(cart) # TODO: Add products not founded to a list and return it
        logging.info(f'Usuario {user.id} con {user.points} puntos está canjeando estos productos {products}')
        # TODO: this function should return a response for the 'canjear' action (a dict with the result of the operation)
