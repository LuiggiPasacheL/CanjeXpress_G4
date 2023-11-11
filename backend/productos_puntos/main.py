import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from application.getProductUseCase import GetProductUseCase
from application.getProductsUseCase import GetProductsUseCase
from infrastructure.adapters.postgresProductsRepository import PostgresProductsRepository
from infrastructure.database import init_db
from ariadne import graphql_sync, make_executable_schema, load_schema_from_path
from ariadne.explorer import ExplorerGraphiQL
from infrastructure.graphqlResolvers import query, mutation

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, mutation)

app = Flask(__name__)
CORS(app)

repository = PostgresProductsRepository()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/products')
def getProducts():
    getProductsUseCase = GetProductsUseCase(repository)
    products = getProductsUseCase.execute()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'pricePoint': product.pricePoint,
        'quantity': product.quantity
    } for product in products])

@app.route('/products/<int:id>')
def get_products(id: int):
    getProductUseCase = GetProductUseCase(repository)
    product = getProductUseCase.execute(id=id)
    if product is None:
        return 'Product not found', 404
    return jsonify({
        'id': product.id,
        'name': product.name,
        'pricePoint': product.pricePoint,
        'quantity': product.quantity
    })


explorer_html = ExplorerGraphiQL().html(None)
@app.route('/graphql', methods=['GET'])
def graphqlPlayground():
    return explorer_html, 200

@app.route('/graphql', methods=['POST'])
def graphqlServer():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == '__main__':
    init_db(app)
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
