from domain.exceptions import PointsMustBePositive, StockMustBePositive, RequiredQuantityMustBePositive

class Product:
    def __init__(self, id: int, points: int, stock: int, requiredQuantity: int):
        if points < 0:
            raise PointsMustBePositive(id, "product")
        if stock < 0:
            raise StockMustBePositive(id, "product")
        if requiredQuantity < 0:
            raise RequiredQuantityMustBePositive(id, "product")
        self.id = id
        self.points = points
        self.stock = stock 
        self.requiredQuantity = requiredQuantity
