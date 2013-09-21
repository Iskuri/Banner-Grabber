import socket
import select

class SocketHandler:
	port = 23
	ip = "127.0.0.1"

	def __init__(self,_ip):
		self.ip = _ip

	def grabBanner(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			s.settimeout(5)
			#print "Starting connection"
			s.connect((self.ip, self.port))
			#print "Connected"
			#s.setblocking(0)
			banner = ''

			ready = select.select([s], [], [], 5)

			while ready[0] and len(banner) < 1000:
				try: 
					banner += s.recv(1)
					#print "Got byte"
				except:
					break

			#print "Saving banner"
			return banner
		except:
			return ''

		
