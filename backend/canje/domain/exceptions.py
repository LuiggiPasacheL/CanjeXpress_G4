
class PointsMustBePositive(Exception):
    def __init__(self):
        self.message = "Points must be positive"

class StockMustBePositive(Exception):
    def __init__(self):
        self.message = "Stock must be positive"

class RequiredQuantityMustBePositive(Exception):
    def __init__(self):
        self.message = "Required quantity must be positive"
