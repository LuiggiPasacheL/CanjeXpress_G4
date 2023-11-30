
from abc import ABC, abstractmethod
from domain.product import Product
from domain.user import User

class UserRepository(ABC):

    @abstractmethod
    def updateUser(self, user: User, products: list[Product]):
        pass
