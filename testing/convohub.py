import threading
import socket
host="192.168.124.6"
port=1000

def start_server():

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen()

    print("socket is listening in host : {} and in port : {}".format(host,port))

    while True:

        client_socket,address=s.accept()

        thread=threading.Thread(target=handle_client,args=(client_socket,address))

        thread.start()



def handle_client(client_socket,address_port):

    print("got connection from {}".format(address_port))

    fullmessage=""

    while True:

        data=client_socket.recv(1024).decode('utf-8')

        if not data:
            print("no message received connection terminated")
            client_socket.close()

        fullmessage+=data

        if "\n" in data:

            final_message=fullmessage.strip()

            if final_message == "exit":

                print("connection terminated")
                client_socket.close()
            
            else:
                
                print("data received from the address {} is {} ".format(address_port,final_message))

                client_socket.send("message received".encode("utf-8"))

                fullmessage=""
                



if __name__  == "__main__":
    
    start_server()
