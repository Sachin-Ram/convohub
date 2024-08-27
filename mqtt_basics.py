#!/usr/bin/env python3

import paho.mqtt.client as mqtt

HOST = 'broker.hivemq.com'
PORT = 1883
TIMEOUT = 60

def on_message(client, userdata, message):
	print("{}: {}".format(message.topic, str(message.payload)))
	
def on_connect(client, userdata, flags, rc):
	print("Connected.")
	client.subscribe('lahtp-sockets-group')

client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

client.connect(HOST, PORT, TIMEOUT)
client.loop_forever()
