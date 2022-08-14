import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPv4 UDP socket

msg = input()

try:
    client.sendto(msg.encode(), ("127.0.0.1", 4433))
    response = client.recvfrom(1024).decode()
    print(response)
except:
    print("Error")
    