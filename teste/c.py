import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "tus es"
client.sendto(msg.encode("utf-8"), ('127.0.0.1', 12345))

data, addr = client.recv(4096)
print(str(data))

client.close()