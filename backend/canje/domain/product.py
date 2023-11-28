from domain.exceptions import PointsMustBePositive, StockMustBePositive, RequiredQuantityMustBePositive

class Product:
    def __init__(self, id: int, points: int, stock: int, requiredQuantity: int):
        if points < 0:
            raise PointsMustBePositive()
        if stock < 0:
            raise StockMustBePositive()
        if requiredQuantity < 0:
            raise RequiredQuantityMustBePositive()
        self.id = id
        self.points = points
        self.stock = stock 
        self.requiredQuantity = requiredQuantity
