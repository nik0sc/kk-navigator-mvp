from flask import Flask, jsonify
import navigation
from map_render import *

from mqtt import MQTT

app = Flask(__name__)

mqtt_service = MQTT()


@app.route('/directions/<start>/<dest>', methods=['GET'])
def directions(start, dest):

    try:
        nodes = navigation.g.shortest_path(start, dest)
        direction = navigation.generate_route(nodes)
        map_render = str(render_map(nodes))
        mqtt_service.publish_msg(str(nodes))
        error_code = ""

    except Exception as e:
        error_code = str(e)

    response = {
        "direction": direction,
        "map_render": map_render,
        "error": error_code
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
