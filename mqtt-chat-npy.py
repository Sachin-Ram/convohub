#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from threading import Thread
import npyscreen

HOST = 'broker.hivemq.com'
PORT = 1883
TIMEOUT = 60
f = None
TOPIC = 'lahtp-sockets-group'

class SubThread(Thread):
	def __init__(self):
		Thread.__init__(self)
		
class ChatForm(npyscreen.SplitForm, npyscreen.ActionForm):
	def create(self):
		client.connect(HOST, PORT, TIMEOUT)
		self.draw_line_at = 18
		self.MOVE_LINE_ON_RESIZE = True
		self.chat_screen = self.add(npyscreen.MultiLine, name="MultiLineChatScreen", height=18)
		self.chat_screen.display()
		self.message_field = self.add(npyscreen.TitleText, name="Send: ", editable=True)
		
	def on_ok(self):
		#npyscreen.notify_confirm(self.message_field.value)
		client.publish(TOPIC, self.message_field.value)
		self.message_field.value = ""
		
		
		
	def on_cancel(self):
		exit(0)
		
	def add_msg(message):
		if(self.chat_screen.value is None):
			self.chat_screen.value = message
		else:
			self.chat_screen.value = self.chat_screen.value + "\n" + message
		self.chat_screen.display()

def on_connect(client, userdata, flags, rc):
	npyscreen.notify("Connection Established", title="Info")

def on_message(client, userdata, message):
	f = open("log.txt", "a")
	f.write(message.payload)
	#npyscreen.notify(message, title="New Message")
	if f is not None:
		f.add_msg(message.payload)
	
class App(npyscreen.NPSAppManaged):
	def onStart(self):
		f = self.addForm("MAIN", ChatForm)

		
if __name__=="__main__":
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	#f.chat_screen.value = "Welcome.\n"
	app = App()
	app.run()