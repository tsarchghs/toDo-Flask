import sqlite3

def createDatabase(path):
	conn = sqlite3.connect(path)
	conn.close()
	print("Database created or already existed")


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
	print("Created User table")

def loginUser(username,password,path):
	conn = sqlite3.connect(path)
	c = conn.cursor()
	users = c.execute("SELECT * FROM User")
	users = c.fetchall()
	print(users)
	conn.close()
	for user in users:
		print(user)
		if user[1] == username:
			if user[2] == password:
				return True
	return False

#print(loginUser("gjergjk71","gjergji.123","db.sqlite3"))