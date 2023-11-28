
from abc import ABC, abstractmethod
from domain.product import Product

class ProductsRepository(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def getProducts(self, productsInfo: list[dict]) -> list[Product]:
        pass

    @abstractmethod
    def updateProducts(self, products: list[Product]):
        pass
