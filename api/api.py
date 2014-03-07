__author__ = 'rike'

import sys
import json
from flask import Flask, request, abort
from services.utility import converter
from services.product import catalog

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
        convert = converter.Converter()
        csv_json = convert.csv_bytes_to_json(request.data)

        products_service = catalog.Catalog()
        result = products_service.create_products(csv_json)

        return result

    except:
        print("Unexpected error:", sys.exc_info()[0])
        abort(500)

if __name__ == "__main__":
    app.run()