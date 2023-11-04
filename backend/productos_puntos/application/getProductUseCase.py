
from application.ports.productsRepository import ProductsRepository
from domain.product import Product

class GetProductUseCase:
    def __init__(self, productRepository: ProductsRepository):
        self.productRepository = productRepository

    def execute(self, id: int) -> Product:
        return self.productRepository.getProduct(id)
