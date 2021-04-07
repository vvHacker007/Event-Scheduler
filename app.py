from flask import Flask,render_template,session,flash,url_for,request,redirect
import pymongo as pm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'1\xd4\xa0\x90\xba1y\xf1$\x94%h\x17\x82\x02\x08'
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
    return render_template("home.html")