# Your Python application code should go here.
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from nick-jenkins-project!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
