from socket import *
serverName = 'localhost'
serverPort = 20000

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('' , serverPort))

while True:
    message, clientAddress = server.recvfrom(2048)
    print(message.decode())
