from flask import Flask, jsonify, request
import navigation
from map_render import *

app = Flask(__name__)


@app.route('/directions/<start>/<dest>', methods=['GET'])
def directions(start, dest):

    nodes = navigation.g.shortest_path(start, dest)

    response = {
        "direction": navigation.generate_route(nodes),
        "map_render": str(render_map(nodes))}

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
