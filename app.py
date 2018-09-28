from flask import Flask, jsonify, request
from table import table
import sutd_navigation

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, world'


@app.route('/directions/<start>/<dest>', methods=['GET'])
def directions(start, dest):
    return jsonify({"direction": sutd_navigation.generate_route(sutd_navigation.g.shortest_path(start, dest))})

if __name__ == "__main__":
    app.run(debug=True)