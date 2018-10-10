import socket

sock = socket.socket()
sock.connect(('localhost', 26015))
sock.send(encode('hello, world!'))

data = sock.recv(1024)
sock.close()

print (data)
