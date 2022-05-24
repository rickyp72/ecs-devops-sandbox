"""Main application file"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def returnString():
    return "This container has been deployed. Type a new Endpoint i.e <url>/something "


@app.route("/<random_string>")
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    return "".join(reversed(random_string))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
