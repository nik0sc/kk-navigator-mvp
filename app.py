from flask import Flask, jsonify, request
import navigation

app = Flask(__name__)


@app.route('/directions/<start>/<dest>', methods=['GET'])
def directions(start, dest):

    response = {"direction": sutd_navigation.generate_route(
        sutd_navigation.g.shortest_path(start, dest))}

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
