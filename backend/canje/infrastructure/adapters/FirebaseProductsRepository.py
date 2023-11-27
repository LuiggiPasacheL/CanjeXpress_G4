
import logging
import firebase_admin
from firebase_admin import firestore
from application.ports.productsRepository import ProductsRepository
from domain.product import Product
from firebase_admin import credentials

class FirebaseProductsRepository(ProductsRepository):

    def __init__(self):
        cred = credentials.Certificate('firebase-credentials.json')
        self.app = firebase_admin.initialize_app(cred)
        self.db = firestore.client()
    
    def getProducts(self, cart: list[dict]) -> list[Product]:
        """
          Get products method receives a list of productsInfo, each productInfo is a dict with the following structure:
          "productsInfo": [
            {
              "product_id": 1,
              "quantity": 1
            },
            {
              "product_id": 2,
              "quantity": 1
            }
          ]
          And returns a list of Product objects (with the points attributes getted from the database)
        """
        products: list[Product] = []
        products_ref = self.db.collection(u'productos')
        for productInCart in cart:
            product_id = productInCart["product_id"]
            requiredQuantity = productInCart["quantity"]

            product_get = products_ref.document(str(product_id)).get()
            if product_get.exists:
                product = product_get.to_dict()
                points = int(product["points"])
                stock = int(product["quantity"])
                product = Product(product_id, points, stock, requiredQuantity)
                products.append(product)
            else:
                logging.error("Product with id " + product_id + " not found")
        return products
