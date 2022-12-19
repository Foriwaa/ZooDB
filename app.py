from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
from projectzoodb import projectzooDB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'projectzoo.db'

#dbobj = projectzooDB()


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        #return "Clicked the button"
        username = request.form.get("user_name")
        password = request.form.get("pass_word")
        dbobj = projectzooDB()
        result = dbobj.checkAccountType(username, password)
        if result == None:
            return "Acoount does not exist"
        elif result[0] == 1:
            return "You're Logged in as Employee"
        elif result[0] == 2:
            return "You're Logged in as Admin"
        else :
            return "You're Logged in as Visitor"      
    else:
        return render_template("login.html")


@app.route('/register')
def register():
    return render_template('register.html')

'''
@app.route('/logindata', methods=['post'])
def logindata():
    username = request.form.get("user_name")
    password = request.form.get("pass_word")
    dbobj = projectzooDB()
    result = dbobj.checkAccountType(username, password)[0]
    #print(result)
    return render_template("logindata.html", username=username, password=password,result=result)
'''