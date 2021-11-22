# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = "<h3>This is a test for Capstone project</h3>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80