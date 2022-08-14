import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 and TCP socket
client.connect(("www.google.com", 80)) # connect google.com at port 80


client.send(b"GET / HTTP/1.1\nHost: www.google.com \n\n\n") # send smsg in binary
received_packets = client.recv(1024).decode() # receive google.com response
#Note that google only accept HTTP requisitions

print(received_packets)
