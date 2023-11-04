
from application.ports.productsRepository import ProductsRepository
from domain.product import Product

class UpdateProductUseCase:
    def __init__(self, productRepository: ProductsRepository):
        self.productRepository = productRepository

    def execute(self, id: int, product: Product) -> Product|None:
        return self.productRepository.updateProduct(id, product)
