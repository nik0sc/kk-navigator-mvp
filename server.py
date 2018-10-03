from flask import Flask, jsonify, request
import navigation
from map_render import *

from mqtt import MQTT

app = Flask(__name__)

mqtt_service = MQTT()


@app.route("/directions", methods=["POST"])
def directions():

    direction = ""
    map_render = ""
    error_code = ""

    if request.method == "POST":
        try: 
            start = request.args.get("start_loc")
            dest = request.args.get("end_loc")

            try:
                nodes = navigation.g.shortest_path(start, dest)
                direction = navigation.generate_route(nodes)
                map_render = str(render_map(nodes))
                mqtt_service.publish_msg(str(nodes))
            except Exception as e:
                error_code = "Routing Error: " + str(e)

        except Exception as e:
            error_code = "Arguments Error: " + str(e)

    response = {
        "direction": direction,
        "map_render": map_render,
        "error": error_code
    }

    return jsonify(response)


if __name__ == "__main__":
    print("[INFO ] Starting Flask server")
    app.run(debug=True)
