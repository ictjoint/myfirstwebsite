from flask import Flask

app = Flask (__name__)


@app.route ("/")
def hello_world():
    return "<p>HELLO World</p>"

@app.route ("/page1")
def hello_country():
    return "<p>HELLO Country</p>"

