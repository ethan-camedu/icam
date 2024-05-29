import socket

UDP_IP = "10.0.0.121" # change to whatever the server host's local ip is
UDP_PORT = 5005

message = "There once was a story about how El Camino was partially shut down from construction"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
finally:
    sock.close()

print("message:", message)
