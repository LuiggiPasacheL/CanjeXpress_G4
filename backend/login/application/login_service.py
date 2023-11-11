from enum import Enum
from typing import Any
import bcrypt
from application.ports.user_repository import UserRepository

class LoginStatus(Enum):
    OK = 1
    BAD_CREDENTIALS = 2
    NOT_FOUND = 3

class LoginService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, username: str, password: str) -> tuple[LoginStatus, dict[str, Any] | None]:
        user = self.user_repository.get_user_by_username(username)
        if user:
            is_correct = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) 
            additional_data = {
                'id': user.id,
                'username': user.username,
                'points': user.points,
                'profile_picture': user.profile_picture,
                'is_admin': user.is_admin
            }
            if is_correct:
                return LoginStatus.OK, additional_data
            else:
                return LoginStatus.BAD_CREDENTIALS, None
        else:
            return LoginStatus.NOT_FOUND, None
