#A python program to create a TCP/IP server program that sends messafes to a client

#importing Modules
import socket

#takes server name and port number
host='localhost'
port=5000

#Create a socket at server side using TCP/IP protocol 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Bind the socket with server and port number
s.bind((host,port))

#allow minimum 1 connetion in the socket
s.listen(1)

#wait till client accepts connection
c, addr =s.accept()

#Display client address
print("Connection from: ",str(addr))

#Send messages to client after encoding it intobinary string
c.send(b"Hello client, How are you")
msg="Bye!"
c.send(msg.encode())

#disconnect the server
c.close()