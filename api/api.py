__author__ = 'rike'

import sys
import json
from flask import Flask, request, abort
app = Flask(__name__)

@app.route("/")
def root():
    return "nrgRetail"


@app.route("/api")
def api():
    return "nrgRetail api"


@app.route("/api/products")
def products():
    return "nrgRetail api.products"


@app.route("/api/products", methods = ['POST'])
def create_products():

    if not request.data:
        abort(400)

    rows = request.data.decode("utf-8").splitlines()

    arr = []
    headers = []

    for header in rows[0].split(','):
        headers.append(header)

    rows.remove(rows[0])

    for row in rows:
        rowItems = {}
        for i, item in enumerate(row.split(',')):
            print(i, item)
            rowItems[headers[i]] = row
        arr.append(rowItems)

    jsonText = json.dumps(arr).replace('\\"', '')

    return jsonText


if __name__ == "__main__":
    app.run()