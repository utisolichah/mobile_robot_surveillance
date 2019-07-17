from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('control.html')

@app.route("/forward")
def forward():
    return "go_forward"

@app.route("/reverse")
def reverse():
    return "go_reverse"

@app.route("/left")
def turn_left():
    return "go_left"

@app.route("/right")
def turn_right():
    return "go_right"

@app.route("/stop")
def stop():
    return "go_stop"

if __name__ == "__main__":
    app.run('0.0.0.0')
