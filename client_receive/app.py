import os
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("[receiver] Connected with result code " + str(rc))
    client.subscribe("sample_topic")

def on_message(client, userdata, msg):
    print("[receiver] got a message: " + str(msg.payload.decode()))
    client.disconnect()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(os.environ["BROKER_HOST"], 1883, 60)
client.loop_forever()
