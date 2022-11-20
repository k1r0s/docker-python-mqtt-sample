import os
import paho.mqtt.client as mqtt

def run():
    print("[sender] will send a message")
    client.publish("sample_topic", "message from sender")
    client.loop_stop()

def on_connect(client, userdata, flags, rc):
    print("[sender] Connected with result code " + str(rc))
    run()

client = mqtt.Client()
client.on_connect = on_connect

client.connect(os.environ["BROKER_HOST"], 1883, 60)
client.loop_start()
