from abc import ABC, abstractmethod
from domain.user import User

class UserQueryRepository(ABC):

    @abstractmethod
    def get_user_by_username(self, username: str) -> User | None:
        pass

    @abstractmethod
    def get_user_points(self, user_id: int) -> int:
        pass

    @abstractmethod
    def user_exists(self, user_id: int) -> bool:
        pass
