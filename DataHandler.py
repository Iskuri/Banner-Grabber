import adodb

class DataHandler:

	conn = None

	def __init__(self):
	
		self.conn = adodb.NewADOConnection('mysql')
		self.conn.Connect('192.168.1.95','root','disappointed1','telnet_banners')
		
	def getRandom(self):

		self.conn.BeginTrans()

		row = self.getRow("SELECT * FROM banners WHERE in_use IS FALSE AND dead_ip IS FALSE AND banner IS NULL ORDER BY RAND() LIMIT 1");

		self.conn.Execute("UPDATE banners SET in_use = TRUE WHERE id = %d" % row['id'])

		self.conn.CommitTrans()
		return row['ip_address']

	def getRow(self, query):

		cursor = self.conn.Execute(query)
                print cursor.GetRowAssoc(0)
		return cursor.GetRowAssoc(0)
	
	def addIp(self, ip_address):
		self.conn.Execute("INSERT INTO banners(ip_address) VALUES ('"+ip_address+"');")
