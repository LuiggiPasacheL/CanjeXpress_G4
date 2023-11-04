
from typing_extensions import Any
from domain.product import Product
from infrastructure.database import db

class ProductDBModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price_point = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def from_model(self, product: Product):
        self.id = product.id
        self.name = product.name
        self.pricePoint = product.pricePoint
        self.quantity = product.quantity

    def to_model(self) -> Product:
        return Product(
            id=self.id,
            name=self.name,
            pricePoint=self.pricePoint,
            quantity=self.quantity
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'pricePoint': self.pricePoint,
            'quantity': self.quantity
        }


