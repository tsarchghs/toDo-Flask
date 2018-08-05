import sqlite3


def createUserModel(path):
	table = "User"
	columns = """
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username TEXT UNIQUE,
		password TEXT,
			 """
	conn = db.connect(path)
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS {}({})".format(table,columns))
	conn.commit()
	conn.close()
