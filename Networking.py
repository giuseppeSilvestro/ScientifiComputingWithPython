# Python has a built-in support for TCP Socket
# first we import and create a new variable for the Socket
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now we can make the call on the web specifying the port number we want to use
# this line won't do anything, apart from estabilishing a connection or returning
# an error if the connection was not estabilished
mysock.connect(('data.pr4e.org', 80))
# the next line prepares a command to get something stored on that webserver
# it is important not to forget the two whitespaces at the end of our command ('\n\n')
# the encode function will allow us to send this command
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# now we can send our request
mysock.send(cmd)

# it is now time to get the data we requested back and work with them
while True:
# this line will give us back all the data stored in that file 512 caracters at the time
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
# after the loop is finished we can close our connection
mysock.close()
