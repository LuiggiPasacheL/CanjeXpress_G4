from enum import Enum
import bcrypt
from application.ports.user_repository import UserRepository

class LoginStatus(Enum):
    OK = 1
    BAD_CREDENTIALS = 2
    NOT_FOUND = 3

class LoginService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, username: str, password: str) -> LoginStatus:
        user = self.user_repository.get_user_by_username(username)
        if user:
            is_correct = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) 
            if is_correct:
                return LoginStatus.OK
            else:
                return LoginStatus.BAD_CREDENTIALS
        else:
            return LoginStatus.NOT_FOUND
