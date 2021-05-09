from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def welcome():
    return (f"Welcome to the RECIPERFECT search API!<br/>")

if __name__ == '__main__':
    app.run()