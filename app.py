from flask import Flask,request,jsonify
import socket 
import requests
import json

app = Flask(__name__)

@app.route('/')
@app.route('/public')
@app.route('/private')
def index():
    response = {
        "request.method": request.method,
        "request.uri":request.url,
        "headers":json.loads(json.dumps({**request.headers})),
        "served_by": socket.gethostname()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


