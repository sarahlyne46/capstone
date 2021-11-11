from flask import Flask

app = Flask(__name__)

@app.route("/")
def blue():
    html = "https://sl-capstone-website.s3.amazonaws.com/bluedeploy/index.html"
    return html

@app.route("/")
def green():
    html = "https://sl-capstone-website.s3.amazonaws.com/greendeploy/index.html"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
