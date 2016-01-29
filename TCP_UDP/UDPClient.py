
from socket import * #Importerer alle funksjoner
#fra modulen socket og bruker dens namespace

serverName = 'hostname' #The IP or URL of the server we want to access
serverPort = 12000 #The port on the server we want to access
clientSocket = socket(AF_INET, SOCK_DGRAM) #Create a socket. AF_INET indicates the use of ipv4, STREAM = TCP
message = raw_input('Type your message: ') #Inputs message from user
clientSocket.sendto(message, (serverName, serverPort)) #Creates a handshake with the server
#modifiedMessage, serveradress = clientSocket.rcvfrom(2048)
#print 'From server: ', modifiedMessage
clientSocket.close()
