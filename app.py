from flask import Flask, render_template, request, redirect, url_for, session
from flaskweek_functions import authenticate
from flaskweek_functions.forms import ExampleForms, UserLogin

from wtforms import Form, validators, StringField, PasswordField

class loginWTF(Form):
    uid = StringField("Email or username", validators=[validators.InputRequired(), validators.Length(min=5, max=15)])
    pwd = PasswordField("Password", validators=[validators.InputRequired(), validators.equal_to('pwd2', message='PASSWORDS DONT MATCH')])
    pwd2 = PasswordField("confirm password", validators=[validators.InputRequired()])

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

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

@app.route("/login", methods=["GET", "POST", "PUT"])
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


@app.route("/loginwtf", methods=["GET", "POST"])
def loginwtf():
    formLoginWTF = loginWTF(request.form)

    if request.method == "POST" and formLoginWTF.validate():
        uid = formLoginWTF.uid.data
        pwd = formLoginWTF.pwd.data
        pwd2 = formLoginWTF.pwd2.data

        if len(uid) < 5 or len(uid) > 15 or not pwd == pwd2:
            # error
            pass 
        print(uid)
        print(pwd)

        if uid == "anto" and pwd == "1234":
            session["loggedin"] = True
            session["uid"] = uid

            return redirect(url_for("secure"))

    return render_template("login/login.html.j2", form=formLoginWTF)
    
    

@app.route("/logout")
@authenticate
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/secure")
@authenticate
def secure():
    return render_template("secure.html.j2")

@app.route("/form_example")
def form_example():
    form = ExampleForms(request.form)
    return render_template("forms/forms_without_macro.html.j2", form=form)

if __name__ == '__main__':
    app.run(debug=True)