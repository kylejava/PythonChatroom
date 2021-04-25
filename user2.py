from socket import *
serverName = 'localhost'
serverPort = 10001

user2 = socket(AF_INET, SOCK_DGRAM)
user2.bind(('', serverPort))

name = input("What is your name: ")

while True:
    message = input("Enter A Message: ")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    m = ("(" + current_time +") " + "From " + name + ": " + message)
    user2.sendto(m.encode(), (serverName,20000))
