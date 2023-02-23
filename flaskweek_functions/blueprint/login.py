from flask import Blueprint, request, render_template, session, redirect, url_for
from flaskweek_functions import authenticate
from flaskweek_functions.forms import loginWTF

MyLogin = Blueprint("login", __name__, template_folder="templates", static_folder="static", static_url_path="assets")

@MyLogin.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        uid = request.form.get("uid", "")
        pwd:int = int(request.form.get("pwd", ""))
        name = request.form.get("name", "")
        mail = request.form.get("mail", "")

        user = {
            "uid" : uid,
            "pwd" : pwd,
            "name": name
        }

        #db.collection(u"Users").document(mail).set(user)

        # get the data
        # check data
        # store data in database
        # redirect to homepage
        return "Données insérées avec succes"
    else : # when GET
        return render_template("login/signup.html.j2")


@MyLogin.route("/login", methods=["GET", "POST"])
def login():
    formLoginWTF = loginWTF(request.form)

    if request.method == "POST" and formLoginWTF.validate():
        uid = formLoginWTF.uid.data
        pwd = formLoginWTF.pwd.data

        #uid is email

        """user = db.collection(u"Users").where("uid", "==", uid).get()
        print("User from db : ")
        print(user)
        
        if len(user) > 0: #and user[0].to_dict()["pwd"] == pwd: # user found
            user = user[0].to_dict()
            if user["pwd"] == pwd:
                session["loggedin"] = True
                session["uid"] = uid
                return redirect(url_for("secure"))"""

        if uid == "antoo" and pwd == "1234":
            session["loggedin"] = True
            session["uid"] = uid
            return redirect(url_for("secure"))
          

    return render_template("login/login.html.j2", form=formLoginWTF)
    
    

@MyLogin.route("/logout")
@authenticate
def logout():
    session.clear()
    return redirect(url_for("index"))