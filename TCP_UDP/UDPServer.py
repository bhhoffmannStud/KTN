
from scoket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) #create a welcoming socket
serverSocket.bind(('',serverPort)) #bind the port to the socket
print 'The server is ready to recieve'
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) #waits for msg to arrive
    sentence = connectionSocket.recv(1024)
    print sentence
    #modifiedMessage = message.upper()
    #serverSocket.sendto(modifiedMessage, clientAddress)
