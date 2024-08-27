#!/usr/bin/env python3


import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 3074

def start_chat_thread(conn, addr):
	t = ChatMsgThread(conn, addr)
	t.start()
	print("Thread created and offloaded connection with IP {}:{}".format(addr[0], addr[1]))
	
class ChatMsgThread(Thread):
	def __init__(self, conn, addr):
		Thread.__init__(self)
		self.conn = conn
		self.addr = addr
		#print("IP {} connected".format(addr[0]))
		
	def run(self):
		self.conn.sendall(b"Send your message, I will be able to see it here.\n")
		while(True):
			try:
				data = self.conn.recv(2048)
				if not data:
					self.conn.close()
					continue
				else:
					try:
						data = data.decode()
						print(data)
					except:
						pass
			except:
				pass
						

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
while(True):
	conn, addr = s.accept()
	#conn - the connection object with the client
	#addr - array 0 - IP address of the client 
	#		array 1 - The back port with which the connection is established
	start_chat_thread(conn, addr)
s.close()


