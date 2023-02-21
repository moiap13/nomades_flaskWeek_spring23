from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

def authenticate(f):
    @wraps(f) 
    def decorated_func(*args, **kwargs):
        if "loggedin" in session and session["loggedin"]:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return decorated_func

@app.route("/")
def index():
    uid = session.get("uid", "")
    return render_template("index.html.j2", uid=uid)

@app.route("/account")
def account():
    l = ["Conrad", "Fabrice", "Monica", "Arnaud"]
    return render_template("account.html.j2", eleves=l)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        uid = request.form.get("uid", "")
        pwd = request.form.get("pwd", "")
        print(uid)
        print(pwd)

        # get the data
        # check data
        # store data in database
        # redirect to homepage
        return "Données récupérées"
    else : # when GET
        return render_template("login/signup.html.j2")

@app.route("/login", methods=["GET", "POST"])
def login():
    if "loggedin" in session and session["loggedin"]:
        return redirect("secure")

    if request.method == "POST":
        uid = request.form.get("uid", "")
        pwd = request.form.get("pwd", "")

        if uid == "anto" and pwd == "1234":
            # user is logged_in
            session["loggedin"] = True
            session["uid"] = uid

            return redirect(url_for("secure"))
        
    return render_template("login/login.html.j2")

@app.route("/logout")
@authenticate
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/secure")
@authenticate
def secure():
    return render_template("secure.html.j2")

if __name__ == '__main__':
    app.run(debug=True)