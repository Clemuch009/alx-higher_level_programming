#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask server is running!"

@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')
    return f"Email received: {email}"

@app.route('/route_json', methods=['POST'])
def route_json():
    data = request.get_json()
    return jsonify({"received": data}), 200

@app.route('/route_6', methods=['POST'])
def route_6():
    return "You successfully reached /route_6 via POST", 200

@app.route('/catch_me', methods=['GET'])
def catch_me():
    return "You got me!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

