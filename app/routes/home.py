from flask import Blueprint, render_template, session, redirect, url_for

home_bp = Blueprint("home", __name__, url_prefix="/")

@home_bp.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("task.dashboard"))
    return render_template("home.html")
