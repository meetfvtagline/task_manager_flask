# task CRUD logic

from flask import Blueprint, render_template

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

@tasks_bp.route("/login")
def login():
    return render_template("auth/register.html")
