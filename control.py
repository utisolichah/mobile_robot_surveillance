from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('control.html')

@app.route("/forward", )
def forward():
    file = open("testfile.text","w")
    file.write("forward")
    file.close()
    return "go_forward"

@app.route("/reverse")
def reverse():
    file = open("testfile.text","w")
    file.write("reverse")
    file.close()
    return "go_reverse"

@app.route("/left")
def turn_left():
    file = open("testfile.text","w")
    file.write("left")
    file.close()
    return "go_left"

@app.route("/right")
def turn_right():
    file = open("testfile.text","w")
    file.write("right")
    file.close()
    return "go_right"

@app.route("/stop")
def stop():
    file = open("testfile.text","w")
    file.write("stop")
    file.close()
    return "go_stop"

if __name__ == "__main__":
    app.run('0.0.0.0')
