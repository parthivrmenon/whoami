from flask import Flask
import socket 
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Version:2.0 ; I am " + socket.gethostname() + "</h1>"

if __name__ == '__main__':
    app.run(debug=True)


