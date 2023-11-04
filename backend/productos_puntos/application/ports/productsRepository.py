
from abc import ABC, abstractmethod
from domain.product import Product

class ProductsRepository(ABC):

    @abstractmethod
    def getProducts(self) -> list[Product]:
        pass

    @abstractmethod
    def getProduct(self, id: int) -> Product:
        pass

    @abstractmethod
    def addProduct(self, product: Product):
        pass

    @abstractmethod
    def updateProduct(self, id: int, product: Product):
        pass

    @abstractmethod
    def deleteProduct(self, id: int):
        pass
