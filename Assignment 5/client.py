import socket
import ipaddress

serverIP = input("Enter server IP Address: ")
serverPort = int(input("Enter server port number: "))
maxBytesToReceive = 1024

myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myTCPSocket.connect((serverIP, serverPort))

while True:
    myMessage = input("Enter a message to send to server: ")
    if myMessage == "exit":
        break
    myTCPSocket.send(bytearray(str(myMessage), encoding='utf-8'))
    serverResponse = myTCPSocket.recv(maxBytesToReceive).decode('utf-8')
    print("Server Response: ", serverResponse)
myTCPSocket.close()