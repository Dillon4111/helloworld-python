from flask import Flask

app = Flask(__name__)

@app.route('/')
def method():
 html = 'Hello World!'
 return html