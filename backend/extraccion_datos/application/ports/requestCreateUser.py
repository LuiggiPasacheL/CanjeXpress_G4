from abc import ABC, abstractmethod

class RequestCreateUser(ABC):

    @abstractmethod
    def sendMessage(self, users: list[dict]):
        pass
