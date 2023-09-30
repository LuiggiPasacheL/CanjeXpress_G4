import bcrypt
from ..infrastructure.user_repository import UserRepository

class LoginService:
    def __init__(self):
        self.user_repository = UserRepository()

    def login(self, username: str, password: str) -> dict:
        user = self.user_repository.get_user_by_username(username)
        if user:
            is_correct = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) 
            if is_correct:
                return {"success": True, "message": "OK"}
            else:
                return {"success": False, "message": "BADCREDENTIALS"}
        else:
            return {"success": False, "message": "NOTFOUND"}
