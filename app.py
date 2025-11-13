# app.py
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/put', methods=['PUT'])
def put():
    data = request.get_json(force=True)
    return jsonify(data), 200


@app.route('/delete', methods=['DELETE'])
def delete():
    return jsonify(message="Deleted")


if __name__ == '__main__':
    app.run(debug=True)
