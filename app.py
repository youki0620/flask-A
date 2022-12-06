from flask import Flask, render_template,request,redirect


import sqlite3,random
app=Flask(__name__)

@app.route("/")
def helloworld():
    return"<h1>Flaskからハローワールド</h1>"

# @app.route("/test")
# def test():
#     return"<h1>これはテスト表示です</h1>"

# @app.route("/<name>")
# def greet(name):
#     return name + "さん、こんにちは"

@app.route("/template")
def template():
    py_name = "あき"
    return render_template("index.html",name = py_name)

@app.route("/weather")
def weather():
    py_weather = "はれ"
    return render_template("/weather.html",tenki = py_weather)

# -----------2日目----------------

@app.route("/color")
def color():
    conn = sqlite3.connect("color.db")
    c = conn.cursor()
    c.execute("select * from colors;")
    py_color = c.fetchall()
    py_color = random.choice(py_color)
    print(py_color)
    c.close()
    return render_template("color.html",iro = py_color)






# -----------3日目------------


@app.route("/add",methods=["GET"])
def add_get():
    return render_template("add.html")

@app.route("/add",methods=["POST"])
def add_post():
    task = request.form.get("task")
    conn = sqlite3.connect("task.db")
    c = conn.cursor()
    c.execute("insert into tasks values(null,?)",(task,))
    conn.commit()
    c.close()
    return"登録完了"

# -----------3日目------------

@app.route("/list")
def list():
    conn = sqlite3.connect("task.db")
    c = conn.cursor()
    c.execute("select id,task from tasks;")
    task_list = []
    for row in c.fetchall():
        task_list.append({"id":row[0], "task":row[1]})
    print(task_list)
    c.close()
    return render_template("list.html",task_list=task_list)

@app.route("/edit/<int:id>")
def edit(id):
    conn = sqlite3.connect("task.db")
    c = conn.cursor()
    c.execute("select task from tasks where id = ?;",(id,))
    task = c.fetchone()
    c.close()
    if task is not None:
        task = task[0]
    else:
        return "タスクがないよ"
    print(task)
    item = {"id":id,"task":task}
    return render_template("edit.html",item = item)


# -----------五日目----------------

@app.route("/edit",methods=["POST"])
def edit_post():
    task_id = request.form.get("task_id")
    task = request.form.get("task")
    conn = sqlite3.connect("task.db")
    c = conn.cursor()
    c.execute("update tasks set task = ? where id = ?",(task,task_id))
    conn.commit()
    c.close()
    return redirect("/list")

@app.route("/del/<int:id>" ,methods=["POST"])
def del_task(id):
    conn = sqlite3.connect("task.db")
    c = conn.cursor()
    c.execute("delete from tasks where id = ?;",(id,))
    conn.commit()
    c.close()
    return redirect("/list")

if __name__=="__main__":
    app.run(debug=True)
