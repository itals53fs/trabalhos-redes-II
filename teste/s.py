import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
comp = ('127.0.0.1', 80)
server.bind(comp)


data, addr = server.recvfrom(4096)
print(str(data))
message = bytes("you burro man").encode('utf-8')
server.sendto(message, addr)