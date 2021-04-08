from flask import Flask,render_template,session,flash,url_for,request,redirect
from dotenv import load_dotenv,find_dotenv
import os
load_dotenv(find_dotenv())

todo = [
    {
        "task":"Study for CT",
        "priority":"2"
    },
    {
        "task":"Go to gym",
        "priority":"1"
    },
    {
        "task":"Go to market",
        "priority":"5"
    },
    {
        "task":"Go for jogging",
        "priority":"3"
    },
]
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
@app.route('/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email_id = request.form['email']
        password = request.form['password']
        if email_id == "user@gmail.com" and password == "admin":
            return redirect(url_for("home"))
        elif email_id != "user@gmail.com":
            flash(f"Email Id is not registered!")
            return render_template("register_base.html")
        elif password != "admin":
            flash(f"Password is incorrect!")
            return render_template("register_base.html")
        return render_template("register_base.html")
    else:
        return render_template("register_base.html")

@app.route('/user/')
def home():
    return render_template("base.html")

@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/todo/',methods=['GET','POST'])
def todo():  
    return render_template("todolist.html",todo=todo)

@app.route('/stats/')
def stats():
    return render_template("stats.html")

@app.route('/notes/')
def notepad():
    return render_template("notepad.html")
