from flask import Flask

app = Flask (__name__)


@app.route ("/")
def home():
    return "<p>Home Page</p>"

@app.route ("/aboutus")
def about_us():
    return "<p>About Us</p>"

@app.route ("/products")
def products():
    return "<p>Our Products</p>"

@app.route ("/services")
def services():
    return "<p>Our Services</p>"


