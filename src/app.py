from flask import Flask, redirect, url_for, session, request
from config import settings
from connector import openAiConnector

app = Flask(__name__)
app.secret_key = b'DEV_KEY'


@app.route("/")
@app.route("/index")
def index():
    return redirect(url_for("selectrole"))


@app.route("/selectrole")
def get_exising_roles():
    return {"title": "Select role", "data": settings.roles}


@app.route("/selectrole", methods=["POST"])
def selectrole():
    selected = request.form.get("role")
    if selected in settings.roles:
        session["role"] = selected
        return redirect(url_for("interact"))
    return {}, 400


@app.route("/interact")
def interact():
    if "role" not in session:
        return redirect(url_for("selectrole"))
    return f"Selected role {session['role']}"


@app.route("/interact", methods=["POST"])
def post_question():
    if "role" not in session:
        return redirect(url_for("selectrole"))
    if not request.form.get("content"):
        return redirect(url_for("interact"))
    connobject = openAiConnector(session["role"], request.form["content"])
    return connobject.connect()
