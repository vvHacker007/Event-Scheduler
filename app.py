from flask import Flask,render_template,session,flash,url_for,request,redirect
from dotenv import load_dotenv,find_dotenv
import os
import requests
load_dotenv(find_dotenv())

todo_list = [
    {
        'id':'0',
        'task':'Nothing',
        'complete':True
    },
    {
        'id':'1',
        'task':'Study for CT',
        'complete':False
    },
    {
        'id':'2',
        'task':'Go to gym',
        'complete':False
    },
    {
        'id':'3',
        'task':'Go to market',
        'complete':False
    },
    {
        'id':'4',
        'task':'Go for jogging',
        'complete':False
    }
]

def search(list,string):
    for i in range(len(list)):
        if list[i]['task'] == string:
            return True
    return False

app = Flask(__name__)
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
    return redirect(url_for('stats'))

@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/todo/')
def todo():
    new_todo = todo_list[1:]
    return render_template("todolist.html",todos=new_todo)

@app.route("/add",methods=["POST"])
def addTodo():
    task = request.form.get("task")
    if search(todo_list,task)==True:
        print("IT IS ALREADY PRESENT!")
    else:
        last_id = int(todo_list[-1]['id']) 
        added_task = {
            'id': str(last_id+1),
            'task':request.form.get("task"),
            'complete':False
            }
        todo_list.append(added_task)
    return redirect(url_for("todo"))

@app.route("/complete/<string:task>")
def completeTodo(task):
    print("THIS IS YOUR TASK: ",task)
    print("NOW")
    task_completion = next(item for item in todo_list if item["task"] == task)
    print(task_completion)
    task_completion['complete'] = not task_completion['complete']
    return redirect(url_for("todo"))

@app.route("/delete/<string:task>")
def deleteTodo(task):
    for i in range(len(todo_list)):
        if todo_list[i]['task'] == task:
            del todo_list[i]
            break    
    return redirect(url_for("todo"))

@app.route('/stats/')
def stats():
    return render_template("stats.html",todo_list=todo_list)

@app.route('/notes/')
def notepad():
    return render_template("notepad.html")


@app.route('/clock/')
def clock():
    return render_template("clock.html")

if __name__ == '__main__':
    app.run(debug=True)
    app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')