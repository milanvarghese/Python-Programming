#A TCP/IP client that receives messages from the server
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

print("Type 'Exit' to exit the chat")
m1,m2='0','0'
while 1:
    m1=c.recv(1024)
    m1.decode()
    if m1!='0':
        print("Client: "+m2)
        m1='0'
    m2=input("Enter Message: ")
    if m2=='Exit' or m2=='exit':
        break
    elif m2=='0':
        continue
    else:
        c.send(m2.encode())
        m1='0'

if m2=='Exit' or m2=='exit':
    s.close()