
from scoket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) #create a welcoming socket
serverSocket.bind(('',serverPort)) #bind the socket to the port
serverSocket.listen(1) #argument is max nr of queued connections
print 'The server is ready to recieve'
while 1:
    connectionSocket, addr = serverSocket.accept() #connection socket established
    #dedicated to the client requesting connection.
    #Handshake happens between clientSocket and connectionSocket
    sentence = connectionSocket.recv(1024)
    print sentence
    connectionSocket.close()
