from flask import Flask,session,request,render_template,redirect,url_for
from flask_bcrypt import Bcrypt
from database import createDatabase,createUserModel,loginUser,usernameExists,createUser

dbPath = "db.sqlite3"
createDatabase(dbPath)
createUserModel(dbPath)

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("auth/login.html")
	elif request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		password_hashed = bcrypt.generate_password_hash(password)
		if loginUser(username,password_hashed,dbPath):
			session["logged_in"] = True
			return redirect("/index")
		else:
			return render_template("auth/login.html",invalid=True)

@app.route("/register",methods=["GET","POST"])
def register():
	if request.method == "GET":
		return render_template("auth/register.html")
	elif request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		password_hashed = bcrypt.generate_password_hash(password)
		if not usernameExists(username,dbPath):
			createUser(username,password_hashed,dbPath)
			return redirect(url_for("login"))
		else:
			return render_template("auth/register.html",invalid=True)


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