from abc import ABC, abstractmethod
from domain.user import User

class UserRepository(ABC):
    @abstractmethod 
    def get_user_by_username(self, username: str) -> User | None:
        pass 

    @abstractmethod
    def update_user_points(self, id: int, points: int) -> None:
        pass

    @abstractmethod
    def update_product_user(self, user_id: int, product_id: int, required_quantity: int) -> None:
        pass
