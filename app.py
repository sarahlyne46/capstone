# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='text-align: center;'>Welcome to my Cloud DevOps Engineer Capstone Project - 18th November!</h1>"


if __name__ == "__main__":
    app.run()