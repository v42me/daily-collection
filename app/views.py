__author__ = 'oliverhuang'

from app import app


app.route("/")


def index():
    return "hello"