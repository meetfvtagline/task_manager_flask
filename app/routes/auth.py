from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.extensions import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if not user or not check_password_hash(user.password, request.form["password"]):
            flash("Invalid credentials")
            return redirect(url_for("auth.login"))

        session["user_id"] = user.id
        session["username"] = user.username
        return redirect(url_for("task.dashboard"))

    return render_template("auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form["email"]).first():
            flash("User already exists")
            return redirect(url_for("auth.register"))

        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=generate_password_hash(request.form["password"])
        )
        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please login.")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

@auth_bp.route("/logout",methods=["POST"])
def logout():
    session.clear()
    response=redirect(url_for("home.home"))
    response.delete_cookie("session")
    return response
