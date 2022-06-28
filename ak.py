
from flask import Flask, redirect, render_template, request, session, url_for
from akash.routers import second

app = Flask(__name__)
app.secret_key = 'akashshinde123'

@app.route("/user",methods=["POST","GET"])
def login():
    # user =request.form["name"]
    return render_template("login.html")

app.register_blueprint(second,url_for="/user")

def login_req(f):
    def wrap():
        if 'login' in session:
            return f()
        else:
            return redirect('/')
    return wrap

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about/")
@login_req
def about():
    return render_template("covid.html")


# @app.route("/login",methods=["POST","GET"])
# def login():
#     if request.method == "POST":
#         user =request.form["name"]
#         return redirect(url_for("user",usr=user))
        
#     return render_template("login.html")





# @app.route("/<usr>")
# def user(usr):
#     return usr




if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)
