from flask import Flask,Blueprint, redirect, render_template, session
from akash.model import User
second = Blueprint("second",__name__,static_folder="../static", template_folder="../templates")


# @second.route("/user",methods=["POST","GET"])
# def login():
#     # user =request.form["name"]
#     return render_template("login.html")

@second.route('/user/signup/', methods=["POST"])
def signup():
    return User().signup()

@second.route('/user/signout')
def signout():
    return User().signout()

@second.route('/user/geta' ,methods=["POST"])
def user():
    return User().user()

@second.route('/user/login', methods=["POST"])
def login():
  return User().login()
