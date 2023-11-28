
class PointsMustBePositive(Exception):
    def __init__(self, id: int, type: str):
        self.message = f"Points must be positive for {type} with id {id}"

class StockMustBePositive(Exception):
    def __init__(self, id: int, type: str):
        self.message = f"Stock must be positive for {type} with id {id}"

class RequiredQuantityMustBePositive(Exception):
    def __init__(self, id: int, type: str):
        self.message = f"Required quantity must be positive for {type} with id {id}"
