
class Product():

    def __init__(self, id: int | None, name: str, pricePoint: int, quantity: int):
        self.id = id
        self.name = name
        self.pricePoint = pricePoint
        self.quantity = quantity
