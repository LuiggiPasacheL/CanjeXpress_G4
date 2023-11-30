from dataclasses import dataclass

@dataclass
class User:
    id: int|None
    username: str
    password: str
    points: int
    profile_picture: str
    is_admin: bool
