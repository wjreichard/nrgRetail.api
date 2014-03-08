from service import product_catalog, utility_uconverter

__author__ = 'rike'

import sys
from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def root():
    return "nrgRetail"


@app.route("/api")
def api():
    return "nrgRetail api"


@app.route("/api/products")
def get_products():
    return "nrgRetail api.products"


@app.route("/api/products", methods = ['POST'])
def create_products():

    if not request.data:
        abort(400)

    try:
        convert = utility_uconverter.Converter()
        csv_json = convert.csv_bytes_to_json(request.data)

        products_service = product_catalog.Catalog()
        result = products_service.create_products(csv_json)

        return result

    except:
        print("Unexpected error:", sys.exc_info()[0])
        abort(500)

if __name__ == "__main__":
    app.run()