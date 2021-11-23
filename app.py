from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<html><head style="background-color: lightblue; font-family:  verdana; color: purple;">Udacity Capstone Project</head><body style="background-color: lightpurple; font-family:  verdana; color: blue;">Capstone Project</body></html>'
    
app.run(host="0.0.0.0", port=8080, debug=True)