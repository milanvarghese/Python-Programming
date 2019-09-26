#A python program to create a TCP/IP server program that sends messafes to a client
import socket
#takes server name and port number
host='localhost'
port=5000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Create a socket at server side using TCP/IP protocol 
s.bind((host,port)) #Bind the socket with server and port number
s.listen(1) #allow minimum 1 connetion in the socket
c, addr =s.accept() #wait till client accepts connection
print("Connection from: ",str(addr)) #Display client address


m1,m2='0','0'
print("Type 'Exit' to exit the chat")
while 1:
    m1=input("Enter Message: ")
    if m1=='Exit' or m1=='exit':
        break
    elif m1=='0':
        continue
    else:
        c.send(m1.encode())
        m1='0'
    m2=c.recv(1024)
    m2.decode()
    if m2!='0':
        print("Client: "+m2)
        m2='0'

if m1=='Exit' or m1=='exit':
    c.close() 