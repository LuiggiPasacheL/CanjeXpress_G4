
from application.ports.productsRepository import ProductsRepository
from domain.product import Product

class CreateProductUseCase:
    def __init__(self, productRepository: ProductsRepository):
        self.productRepository = productRepository

    def execute(self, product: Product) -> Product|None:
        return self.productRepository.addProduct(product)
