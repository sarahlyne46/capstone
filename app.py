from flask import Flask

app = Flask(__name__)

def html(content):  # Also allows you to set your own <head></head> etc
   return '<html><head style="background-color: lightblue; font-family:  verdana; color: purple;">Udacity Capstone Project</head><body style="background-color: lightpurple; font-family:  verdana; color: blue;">Capstone Project</body></html>'

@app.route("/")
def index():
    return html
    
app.run(host="0.0.0.0", port=8080, debug=True)