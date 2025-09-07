from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)
SERVICE_A_URL = os.environ.get("SERVICE_A_URL", "http://service_a:5000/ping")

@app.route("/call")
def call():
    resp = requests.get(SERVICE_A_URL, timeout=5)
    data = resp.json()
    return jsonify(caller="service_b", service_a=data.get("message"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
