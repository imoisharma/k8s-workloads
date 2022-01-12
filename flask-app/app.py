from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("This lab is created by M. Sharma")
    return 'Hello, Docker Lovers!'
