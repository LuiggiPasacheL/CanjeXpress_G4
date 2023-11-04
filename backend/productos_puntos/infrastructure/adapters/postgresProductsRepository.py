
from application.ports.productsRepository import ProductsRepository
from domain.product import Product

from infrastructure.productDBModel import ProductDBModel

class PostgresProductsRepository(ProductsRepository):

    def getProducts(self) -> list[Product]:
        productsDB = ProductDBModel().query.all()
        products = map(lambda productDB: productDB.to_model(), productsDB)
        return list(products)

    def getProduct(self, id: int) -> Product|None:
        productDB = ProductDBModel().query.get(id)
        if productDB is None:
            return None
        product = productDB.to_model()
        return product

    def addProduct(self, product: Product):
        productDB = ProductDBModel()
        productDB.from_model(product)
        productDB.query.add_entity(productDB)

    def updateProduct(self, id: int, product: Product):
        productDB = ProductDBModel()
        productDB.from_model(product)
        # productDB.query.filter_by(id=id).update(productDB)

    def deleteProduct(self, id: int):
        ProductDBModel().query.filter_by(id=id).delete()

