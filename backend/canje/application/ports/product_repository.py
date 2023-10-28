from abc import ABC, abstractmethod
from domain.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass
    
    
    @abstractmethod
    def deduct_product_quantity(self, product_id: int, quantity: int):
        """Deducts the quantity of the exchanged product."""
        pass
