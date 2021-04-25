from socket import *
serverName = 'localhost'
serverPort = 10001

user2 = socket(AF_INET, SOCK_DGRAM)
user2.bind(('', serverPort))

while True:
    message, clientAddress = user2.recvfrom(2048)
    print(message.decode())
