from flask import Flask, jsonify

app = Flask(__name__)

table = {
    ('a', 'b'): [
        'a to c',
        'c to b'
    ],
    ('b', 'a'): [
        'b to c',
        'c to a'
    ]
}

@app.route('/hello')
def hello():
    return 'Hello, world'

@app.route('/directions/<start>/<dest>')
def directions(start, dest):
    return jsonify(table.get((start, dest), 'No directions found'))