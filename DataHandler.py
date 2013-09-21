import adodb

class DataHandler:

	conn = None

	def __init__(self):
	
		self.conn = adodb.NewADOConnection('mysql')
		self.conn.Connect('192.168.1.95','root','disappointed1','telnet_banners')
		
	def getRandom(self):

		self.conn.BeginTrans()

		row = self.conn.GetRow("SELECT * FROM banners ORDER BY RAND() LIMIT 1");
		print row

		self.conn.Execute("UPDATE banners SET in_use = TRUE WHERE id = " + str(row['id']))

		self.conn.CommitTrans()
		return row['ip_address']
