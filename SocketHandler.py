import socket

class SocketHandler:
	port = 23
	ip = "127.0.0.1"

	def __init__(self,_ip):
		ip = _ip

	def grabBanner(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ip, self.port))

