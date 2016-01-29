import time
import datetime
from socket import *

# Get the server hostname and port as command line arguments                    
host = 'localhost'
port = 12000
timeout = 1 # in seconds
 
# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM) #Create a socket. AF_INET indicates the use of ipv4, DGRAM = UDP

# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

# FILL IN END

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description
    currentTime = time.asctime()
    data = "Ping " + str(ptime) + " " + str(currentTime)
    
    try:
    	# FILL IN START
	# Record the "sent time"
	sentTime = time.time()

	# Send the UDP packet with the ping message     
        clientSocket.sendto(data, (host, port))
	# Receive the server response
	serverMessage, raddr = clientSocket.recvfrom(2048)
	# Record the "received time"
        recievedTime = time.time()
	# Display the server response as an output
        print serverMessage
        # Round trip time is the difference between sent and received time
        print "RTT: ", recievedTime - sentTime
        
        # FILL IN END
    except:
        # Server does not response
	# Assume the packet is lost
        #print "Request timed out."
        continue

# Close the client socket
clientSocket.close()
 
