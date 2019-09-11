#A TCP/IP client that receives messages from the server

#importing modules
import socket

#take servername and port number
host='localhost'
port=5000

#create a client side socked using TCP/IP protocol 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting it to server and port number
s.connect((host, port))

#Receive message string from server, at a time 1024 B
msg=s.recv(1024)

#Repeat as long as message strings are not empty
while msg:
    print("Received: "+msg.decode())
    msg=s.recv(1024)

#Disconnecting the client
s.close()