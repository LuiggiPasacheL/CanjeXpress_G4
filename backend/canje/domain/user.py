from domain.exceptions import PointsMustBePositive

class User:
    def __init__(self, id, points):
        if points < 0:
            raise PointsMustBePositive(id, "user")
        self.id = id
        self.points = points
