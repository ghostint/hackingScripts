import sys
import socket

website = str(sys.argv[1])
print socket.gethostbyname(website)

