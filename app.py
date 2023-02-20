from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<nom>/<int:age>")
def index(nom, age):
    nom = "</h1><h2>{}</h2>".format(nom)
    return render_template("index.html", nom=nom, age=age)

@app.route("/account2")
def account():
    return render_template("account.html")

if __name__ == '__main__':
    app.run(debug=True)