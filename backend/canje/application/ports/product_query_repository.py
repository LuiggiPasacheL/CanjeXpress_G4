from abc import ABC, abstractmethod
from domain.product import Product

class ProductQueryRepository(ABC):

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass
