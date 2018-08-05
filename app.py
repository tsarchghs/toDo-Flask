from flask import Flask,session,request,render_template
from database import createDatabase,createUserModel

dbPath = "db.sqlite3"
createDatabase(dbPath)
createUserModel(dbPath)

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method == "GET":
		return render_template("auth/login.html")
	elif request.method == "POST":
		return "POST"

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