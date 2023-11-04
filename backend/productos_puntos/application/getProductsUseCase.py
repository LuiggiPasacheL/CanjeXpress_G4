
from application.ports.productsRepository import ProductsRepository
from domain.product import Product

class GetProductsUseCase:
    def __init__(self, productRepository: ProductsRepository):
        self.productRepository = productRepository

    def execute(self) -> list[Product]:
        return self.productRepository.getProducts()
