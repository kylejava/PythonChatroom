from socket import *
serverName = 'localhost'
serverPort = 10000
user1 = socket(AF_INET, SOCK_DGRAM)
user1.bind(('', serverPort))


name = input("What is your name: ")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print(modifiedMessage)
    message = input("Enter A Message: ")
    user1.sendto(message.encode(), 10001)
