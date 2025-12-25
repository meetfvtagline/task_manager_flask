from flask import Blueprint, redirect, url_for, session, render_template

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("task.dashboard"))
    return render_template("home.html")
