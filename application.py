from sun import *
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def result():
    s = calculate(request.form.get("address"))
    if len(s) == 0:
        print("wait a second")
        return render_template("error.html")
    return render_template("result.html",sunrise = s[0],sunset = s[1], location = s[2])

