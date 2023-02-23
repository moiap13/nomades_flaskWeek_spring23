from flask import session, redirect, url_for
from functools import wraps

def authenticate(f):
    @wraps(f) 
    def decorated_func(*args, **kwargs):
        if "loggedin" in session and session["loggedin"]:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return decorated_func