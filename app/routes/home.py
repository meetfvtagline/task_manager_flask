from flask import Blueprint, redirect, url_for, session, render_template
from app.routes.auth import login_required

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    # If logged in → go to dashboard
    if "username" in session:
        return redirect(url_for("task.dashboard"))

    # If logged out → show landing page
    return render_template("home.html")