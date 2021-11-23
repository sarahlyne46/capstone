from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome, My name is Sarah, This is Udacity Final project initial deployment version 2"

app.run(host="0.0.0.0", port=8080, debug=True)