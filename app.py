from flask import Flask,session,request,render_template,redirect,url_for
from database import createDatabase,createUserModel,loginUser,usernameExists,createUser,createToDoModel
from database import createToDo,getToDos,deleteToDo
import bcrypt
import os

dbPath = "db.sqlite3"
createDatabase(dbPath)
createUserModel(dbPath)
createToDoModel(dbPath)
app = Flask(__name__)

app.secret_key = os.urandom(12)

@app.route("/index",methods=["GET","POST"])
def index():
	try:
		session["logged_in"]
	except KeyError:
		session["logged_in"] = False
	if session["logged_in"]:
		if request.method == "POST":
			description = request.form["description"]
			createToDo(session["user_id"],description,dbPath)
			return redirect(url_for("index"))
		toDos = getToDos(session["user_id"],dbPath)
		print(toDos)
		return render_template("index.html",toDos=toDos)
	else:
		return redirect(url_for("login"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
	try:
		session["logged_in"]
	except KeyError:
		session["logged_in"] = False
	if session["logged_in"]:
		deleteToDo(session["user_id"],todo_id,dbPath)
		return redirect(url_for("index"))
	else:
		return redirect(url_for("login"))


@app.route("/login",methods=["GET","POST"])
def login():
	try:
		session["logged_in"]
	except KeyError:
		session["logged_in"] = False
	if not session["logged_in"]:
		if request.method == "GET":
			return render_template("auth/login.html")
		elif request.method == "POST":
			username = request.form["username"]
			password = request.form["password"]
			user = loginUser(username,password,dbPath)
			if user:
				session["logged_in"] = True
				session["user_id"] = user[0]
				return redirect(url_for("index"))
			else:
				return render_template("auth/login.html",invalid=True)
	else:
		return redirect(url_for("index"))

@app.route("/logout")
def logout():
	session["logged_in"] = False
	del session["user_id"]
	return redirect(url_for("login"))

@app.route("/register",methods=["GET","POST"])
def register():
	try:
		session["logged_in"]
	except KeyError:
		session["logged_in"] = False
	if not session["logged_in"]:

		if request.method == "GET":
			return render_template("auth/register.html")
		elif request.method == "POST":
			username = request.form["username"]
			password = request.form["password"]
			password_hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
			if not usernameExists(username,dbPath):
				createUser(username,password_hashed,dbPath)
				return redirect(url_for("login"))
			else:
				return render_template("auth/register.html",invalid=True)
	else:
		return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(debug=True,port=8080)


"""

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
"""
