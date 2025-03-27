# server.py
import socket

serverIP = input("Enter server IP Address: ")
serverPort = int(input("Enter server port number: "))

myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myTCPSocket.bind((serverIP, serverPort))
myTCPSocket.listen(5)
incomingSocket, incomingAddress = myTCPSocket.accept()
maxBytesToReceive = 1024

while True:
    myData = incomingSocket.recv(maxBytesToReceive).decode('utf-8')
    if not myData:
        break
    print("Client says: ", myData)
    myMessage = input("Enter a message to send to client: ")
    incomingSocket.send(bytearray(str(myMessage), encoding="utf-8"))

incomingSocket.close()
myTCPSocket.close()
