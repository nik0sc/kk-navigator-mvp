import paho.mqtt.client as mqtt
import os
import ssl
import argparse
import time

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

usetls = True
tlsVersion = None
port = 8883

mqttc = mqtt.Client()

cert_required = ssl.CERT_REQUIRED
cacerts = "/etc/ssl/certs/"
certfile = "keys/cert.pem"
keyfile = "keys/privkey.pem"

mqttc.tls_set(ca_certs=cacerts, certfile=None, keyfile=None, cert_reqs=cert_required, tls_version=tlsVersion)

mqttc.username_pw_set("ubuntu", "sutd1234")

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.on_log = on_log

host = "metric.team-lol.tk"
keepalive = 60

topic = "kk_metrics"
qos = 0

print("Connecting to "+host+" port: "+str(port))
mqttc.connect(host, port, keepalive)

mqttc.loop_start()

for x in range (0, args.nummsgs):
    msg_txt = '{"msgnum": "'+str(x)+'"}'
    print("Publishing: "+msg_txt)
    infot = mqttc.publish(topic, msg_txt, qos=qos)
    infot.wait_for_publish()

    time.sleep(args.delay)

mqttc.disconnect()