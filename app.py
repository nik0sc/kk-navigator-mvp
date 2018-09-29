from flask import Flask, jsonify, request
import navigation

app = Flask(__name__)


@app.route('/directions/<start>/<dest>', methods=['GET'])
def directions(start, dest):

    response = {"direction": navigation.generate_route(
        navigation.g.shortest_path(start, dest))}

    return jsonify(response)

def generating_graph_matplotlib(start, dest):
    return navigation.g.shortest_path(start, dest)

if __name__ == "__main__":
    app.run(debug=True)
