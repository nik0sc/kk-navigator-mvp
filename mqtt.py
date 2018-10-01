import paho.mqtt.client as mqtt
import time


class MQTT(object):

    def __init__(self):
        self.host = "3.0.64.224"
        self.port = 8883
        self.keepalive = 60
        self.topic = "kk_metrics"
        self.qos = 0

        self.mqttc = mqtt.Client()

        self.mqttc.username_pw_set("ubuntu", "sutd1234")

        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_publish = self.on_publish
        self.mqttc.on_subscribe = self.on_subscribe
        self.mqttc.on_log = self.on_log

        print("[ INFO] Connecting to "+self.host+" port: "+str(self.port))

        self.mqttc.connect(self.host, self.port, self.keepalive)

        print("[ INFO] SUCCESS")

        self.mqttc.loop_start()

    def publish_msg(self, msg):
        infot = self.mqttc.publish(self.topic, msg, qos=self.qos)
        infot.wait_for_publish()
        print("Published:", msg)

    def on_connect(mqttc, obj, flags, rc):
        print("connect rc: " + str(rc))

    def on_message(mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

    def on_publish(mqttc, obj, mid):
        print("mid: " + str(mid))

    def on_subscribe(mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(mqttc, obj, level, string):
        print(string)

    def __del__(self):
        self.mqttc.disconnect()


if __name__ == "__main__":
    mqtt_service = MQTT()
    mqtt_service.publish_msg("Test message from __main__")
