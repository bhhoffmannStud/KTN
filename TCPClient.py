
from socket import * #Importerer alle funksjoner
#fra modulen socket og bruker dens namespace

serverName = 'hostname' #The IP or URL of the server we want to access
serverPort = 12000 #The port on the server we want to access
clientSocket = socket(AF_INET, SOCK_STREAM) #Create a socket. AF_INET indicates the use of ipv4, STREAM = TCP
clientSocket.connect((serverName, serverPort)) #Creates a handshake with the server
message = raw_input('Type your message: ') #Inputs message from user
clientSocket.send(message) #Transmitts the message
#modifiedMessage = clientSocket.rcvfrom(1024)
#print 'From server: ', modifiedMessage
clientSocket.close()
