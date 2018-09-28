from flask import Flask, jsonify
from table import table

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, world'


@app.route('/directions/<start>/<dest>')
def directions(start, dest):
    return jsonify(table.get((start, dest), 'No directions found'))
