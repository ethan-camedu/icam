import socket

UDP_IP = "10.0.0.26" # change to your local ip
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received packet from {addr}: {data.decode('utf-8')}")
