
from ariadne import ObjectType
from application.getProductUseCase import GetProductUseCase
from application.getProductsUseCase import GetProductsUseCase
from infrastructure.adapters.postgresProductsRepository import PostgresProductsRepository

query = ObjectType("Query")

repository = PostgresProductsRepository()
getProductUseCase = GetProductUseCase(repository)
getProductsUseCase = GetProductsUseCase(repository)

@query.field("hello")
def resolve_hello(*_):
    return "Hello, GraphQL!"

@query.field("product")
def resolve_product(*_, id: int):
    product = getProductUseCase.execute(id=id)
    if product is None:
        return None
    return {
        'id': product.id,
        'name': product.name,
        'pricePoint': product.pricePoint,
        'quantity': product.quantity
    }

@query.field("products")
def resolve_products(*_):
    products = getProductsUseCase.execute()
    return list(map(lambda product: {
        'id': product.id,
        'name': product.name,
        'pricePoint': product.pricePoint,
        'quantity': product.quantity
    }, products))
