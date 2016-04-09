#!/usr/bin/python

#SERVER
import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() 
s.bind((host, 1870))        

s.listen(10)                
while True:
   c, addr = s.accept()     
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                

#CLIENT
import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() # Get local machine name
s.connect((host, 1870))
print s.recv(1024)
s.close                     # Close the socket when done



