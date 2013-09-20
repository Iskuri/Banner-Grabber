import socket

class SocketHandler:
	port = 23
	ip = "127.0.0.1"

	def __init__(self, _ip):
		ip = _ip

	def grabBanner():
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(ip, port)
		#s.listen(1)

