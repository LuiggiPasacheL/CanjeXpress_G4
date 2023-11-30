
from application.ports.user_repository import UserRepository


class UserService:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    def get_user(self, user_id: int):
        return self.userRepository.get_user_by_id(user_id)

    # def create_user(self, user):
    #     return self.userRepository.create_user(user)
    #
    # def update_user(self, user):
    #     return self.userRepository.update_user(user)
    #
    # def delete_user(self, user_id):
    #     return self.userRepository.delete_user(user_id)
