from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Sarah Lyne Capstone</title>
    <style>
    body{background-color: lightgreen; font-family:  verdana; color: darkgreen;}
	</style>
    </head>
    <body>
    <h1>Hello World!</h1>
    <h2>My name is Sarah Lyne</h2>
    <p> This is my blue deployment for the Capstone Project</p>
    </body>
    </html>
    """
    
    
app.run(host="0.0.0.0", port=8080, debug=True)
