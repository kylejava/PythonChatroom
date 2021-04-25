from socket import *
import time
from datetime import datetime

serverName = 'localhost'
serverPort = 10000
user1 = socket(AF_INET, SOCK_DGRAM)
user1.bind(('', serverPort))


name = input("What is your name: ")
while True:
    #message, clientAddress = user1.recvfrom(2048)
    message = input("Enter A Message: ")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    m = ("(" + current_time +") " + "From " + name + ": " + message)
    user1.sendto(m.encode(), (serverName,20000))
