import sys, traceback
from flask import Flask, request, abort
from config import config
import logging
from service import product_catalog


app = Flask(__name__)

logger = logging.getLogger('api')

@app.route("/")
def root():
    return "nrgRetail"


@app.route("/api")
def api():
    return "nrgRetail api"


@app.route("/api/products", methods=['GET'])
def get_products():

    try:
        return product_catalog.get_active_products()

    except:
        print("/api/products - get_products() - Unexpected error:", sys.exc_info()[0])
        abort(500)


@app.route("/api/products", methods=['POST'])
def create_products():

    if not request.data:
        abort(400)

    try:
        return product_catalog.create_products_from_bytes(request.data)

    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        message = '/api/products - create_products() - Error: {0} - {1} - {2}'\
            .format(exc_type, exc_value, traceback.print_exc())
        logger.error(message)
        return message, 500

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = int(config.server_port), debug = True)