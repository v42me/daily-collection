__author__ = 'oliverhuang'

from app import app
from getAmazon import getData
from flask import render_template
@app.route("/book")
def book():
    items = getData()
    return render_template("book.html",items = items)

@app.route("/")
def hello():
    return render_template("index.html")
