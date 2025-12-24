# login, register, logout

from flask import Blueprint, render_template,request,flash,redirect,url_for
from app.models.user import User
from app.extensions import db
from werkzeug.security import generate_password_hash


dash_page=Blueprint("dashboard",__name__,url_prefix="/")
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")



@dash_page.route("/")
def home():
    return render_template("base.html")


@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")

@auth_bp.route("/register",methods=['POST','GET'])
def register():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']

        existing_user=User.query.filter_by(email=email).first()
        if existing_user:
            flash("User Alrady Exist")
            return redirect(url_for("auth.register"))
        
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.login"))


    return render_template("auth/register.html")


