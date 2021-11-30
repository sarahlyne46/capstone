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
    body{background-color: lightblue; font-family:  verdana; color: purple;}
	</style>
    </head>
    <body>
    <h1>Hello World!</h1>
    </body>
    </html>
    """
    
    
app.run(host="0.0.0.0", port=8080, debug=True)





