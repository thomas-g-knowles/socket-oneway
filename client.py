import socket
from time import sleep

sock = socket.socket()
sock.connect(('127.0.0.1', 12345))
print("- Connection established with socket.")

while True:
	data = ""
	while data == "":
		data = input("- SEND: ")

	if data == "TERMINATE":
		sock.send(data.encode())
		break

	sock.send(data.encode())

sock.close()
print("- - Connection to socket closed; script termination imminent...")
for second in range(5, 0, -1):
  print("- -", second)
  sleep(1)
