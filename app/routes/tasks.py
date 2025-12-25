from flask import Blueprint, render_template, redirect, url_for, session, request
from app.models.task import Task
from app.extensions import db

tasks_bp = Blueprint("task", __name__, url_prefix="/tasks")

@tasks_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    tasks = Task.query.filter_by(user_id=session["user_id"]).all()
    return render_template("tasks/dashboard.html", tasks=tasks)


@tasks_bp.route("/add-task", methods=["POST"])
def add_task():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    task = Task(
        title=request.form["title"],
        description=request.form["description"],
        user_id=session["user_id"]
    )

    db.session.add(task)
    db.session.commit()
    return redirect(url_for("task.dashboard"))


@tasks_bp.route("/update-task/<int:id>", methods=["POST"])
def update_task(id):
    task = Task.query.get_or_404(id)

    if task.user_id != session.get("user_id"):
        return "Unauthorized", 403

    task.status = request.form["status"]
    db.session.commit()
    return redirect(url_for("task.dashboard"))


@tasks_bp.route("/delete-task/<int:id>")
def delete_task(id):
    task = Task.query.get_or_404(id)

    if task.user_id != session.get("user_id"):
        return "Unauthorized", 403

    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("task.dashboard"))
