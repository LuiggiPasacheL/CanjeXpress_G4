from abc import ABC, abstractmethod
from domain.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> User | None:
        pass
    
    @abstractmethod
    def get_user_points(self, user_id: int) -> int:
        """Retrieves the current points for the user with the given ID."""
        pass

    @abstractmethod
    def deduct_points(self, user_id: int, points: int):
        """Deducts the specified number of points from the user with the given ID."""
        pass
    @abstractmethod
    def user_exists(self, user_id: int) -> bool:
        """
      
        """
        pass

