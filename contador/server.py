#ACTIVIDAD CONTADOR 
from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key = "pony puppy"


@app.route("/")
def index():
    if "contador" not in session:
        session["contador"] = 0
    return render_template("index.html")

@app.route("/aumenta")
def aumenta():
    session["contador"] += 1
    return redirect("/")


@app.route("/aumenta/doble")
def aumenta_doble():
    session["contador"] += 2
    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/destroy_session")
def destroy_session():
    session.pop( "contador")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5006)