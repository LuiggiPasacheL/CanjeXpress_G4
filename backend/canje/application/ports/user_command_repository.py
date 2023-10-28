from abc import ABC, abstractmethod

class UserCommandRepository(ABC):

    @abstractmethod
    def deduct_points(self, user_id: int, points: int):
        pass
