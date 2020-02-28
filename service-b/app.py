from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    data = requests.get("http://service-a:5000").json()
    return jsonify("This is service-b, requesting service-a ... ", data), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
