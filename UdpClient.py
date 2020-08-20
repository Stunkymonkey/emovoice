import socket

IP = "192.168.0.111"
port = 12000

def send(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.sendto(message, (IP, port))