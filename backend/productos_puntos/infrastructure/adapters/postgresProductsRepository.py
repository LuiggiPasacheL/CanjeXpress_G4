
from application.ports.productsRepository import ProductsRepository
from domain.product import Product

from infrastructure.productDBModel import ProductDBModel
from infrastructure.database import db

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

    def addProduct(self, product: Product) -> Product|None:
        try:
            productDB = ProductDBModel()
            productDB.from_model(product)
            db.session.add(productDB)
            db.session.commit()
            db.session.refresh(productDB)
            return productDB.to_model()
        except Exception as e:
            print(f"Error al insertar producto: {str(e)}")
            db.session.rollback()
            return None
        finally:
            db.session.close()

    def updateProduct(self, id: int, product: Product) -> Product|None:
        productDB = ProductDBModel().query.get(id)
        if productDB is None:
            return None
        productDB.from_model(product)
        db.session.commit()
        return productDB.to_model()

    def deleteProduct(self, id: int):
        ProductDBModel().query.filter_by(id=id).delete()

