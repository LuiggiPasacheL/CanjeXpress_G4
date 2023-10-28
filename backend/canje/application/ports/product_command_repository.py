from abc import ABC, abstractmethod

class ProductCommandRepository(ABC):

    @abstractmethod
    def deduct_product_quantity(self, product_id: int, quantity: int):
        pass

    @abstractmethod
    def register_exchange(self, user_id: int, cart: list, total_points: int):
        pass
