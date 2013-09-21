import SocketHandler
from SocketHandler import SocketHandler
from DataHandler import DataHandler

socksHandler = SocketHandler('127.0.0.1')
#socksHandler.grabBanner()

dataHandler = DataHandler()
dataHandler.getRandom()
