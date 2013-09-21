import SocketHandler
from SocketHandler import SocketHandler
from DataHandler import DataHandler
import sys


while True:
	dataHandler = DataHandler()
	ip = dataHandler.getRandom()

	if ip == "":
		print "Could not find any ips that need processing"
		sys.exit()

	print "Processing "+ip

	socksHandler = SocketHandler(ip)
	banner = socksHandler.grabBanner()

	#Yes I understand that this is an awful hack
	banner = banner.replace("'","\'")

	dataHandler.setBanner(ip, banner)
