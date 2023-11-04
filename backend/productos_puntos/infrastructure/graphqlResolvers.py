
from ariadne import ObjectType, MutationType
from application.getProductUseCase import GetProductUseCase
from application.getProductsUseCase import GetProductsUseCase
from application.createProductUseCase import CreateProductUseCase
from application.updateProductUseCase import UpdateProductUseCase
from domain.product import Product
from infrastructure.adapters.postgresProductsRepository import PostgresProductsRepository

query = ObjectType("Query")

repository = PostgresProductsRepository()

getProductUseCase = GetProductUseCase(repository)
getProductsUseCase = GetProductsUseCase(repository)
createProductUseCase = CreateProductUseCase(repository)
updateProductUseCase = UpdateProductUseCase(repository)

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

mutation = MutationType()

@mutation.field("createProduct")
def resolve_create_product(*_, name: str, pricePoint: int, quantity: int):
    product = Product(id=None, name=name, pricePoint=pricePoint, quantity=quantity)
    newProduct = createProductUseCase.execute(product=product)
    if newProduct is None:
        return None
    return {
        'id': newProduct.id,
        'name': newProduct.name,
        'pricePoint': newProduct.pricePoint,
        'quantity': newProduct.quantity
    }

@mutation.field("updateProduct")
def resolve_update_product(*_, id: int, name: str, pricePoint: int, quantity: int):
    product = Product(id=id, name=name, pricePoint=pricePoint, quantity=quantity)
    updatedProduct = updateProductUseCase.execute(id=id, product=product)
    if updatedProduct is None:
        return None
    return {
        'id': updatedProduct.id,
        'name': updatedProduct.name,
        'pricePoint': updatedProduct.pricePoint,
        'quantity': updatedProduct.quantity
    }

# @mutation.field("deleteProduct")
# def resolve_delete_product(*_, id: int):
#     product = deleteProductUseCase.execute(id=id)
#     return {
#         'id': product.id,
#         'name': product.name,
#         'pricePoint': product.pricePoint,
#         'quantity': product.quantity
#     }
