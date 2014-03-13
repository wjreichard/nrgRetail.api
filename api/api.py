__author__ = 'rike'

from service import product_catalog
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


@app.route("/api/products", methods=['POST'])
def create_products():

    if not request.data:
        abort(400)

    try:
        #csv_json = utility_converter.csv_bytes_to_json(request.data)
        #result = product_catalog.create_products_from_json(csv_json)
        result = product_catalog.create_products_from_bytes(request.data)

        return result

    except:
        print("Unexpected error:", sys.exc_info()[0])
        abort(500)


if __name__ == "__main__":
    app.run()