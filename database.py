import sqlite3

def createDatabase(path):
	conn = sqlite3.connect(path)
	conn.close()

def createUserModel(path):
	table = "User"
	columns = """
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username TEXT UNIQUE,
		password TEXT
			 """
	conn = sqlite3.connect(path)
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS {}({});".format(table,columns))
	conn.commit()
	conn.close()
