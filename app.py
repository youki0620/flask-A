from flask import Flask, render_template
app=Flask(__name__)

import sqlite3,random

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



if __name__=="__main__":
    app.run(debug=True)