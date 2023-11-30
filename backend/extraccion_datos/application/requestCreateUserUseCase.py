
import logging

from application.ports.requestCreateUser import RequestCreateUser

class RequestCreateUserUseCase:
    def __init__(self, requestCreateUser: RequestCreateUser):
        self.requestCreateUser = requestCreateUser

    def execute(self, users: list[dict]):
        logging.info(f"Request for create user sended: {len(users)} users")

        # TODO: Validate the dict structure before send the message
        # Dict structure: [ {username,password,points,profile_picture,is_admin} ]

        return self.requestCreateUser.sendMessage(users)
