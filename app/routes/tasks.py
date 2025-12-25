from flask import Blueprint, render_template, request, session, jsonify
from app.models.task import Task
from app.extensions import db
from app.routes.auth import login_required

tasks_bp = Blueprint("task", __name__, url_prefix="/tasks")

@tasks_bp.route("/dashboard")
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=session["user_id"]).all()

    counts = {
        "pending": sum(t.status == "pending" for t in tasks),
        "in_progress": sum(t.status == "in-progress" for t in tasks),
        "completed": sum(t.status == "completed" for t in tasks),
    }

    return render_template("tasks/dashboard.html", tasks=tasks, counts=counts)

@tasks_bp.route("/add", methods=["POST"])
@login_required
def add_task():
    task = Task(
        title=request.form["title"],
        description=request.form["description"],
        user_id=session["user_id"]
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(success=True)

@tasks_bp.route("/update/<int:id>", methods=["POST"])
@login_required
def update_task(id):
    task = Task.query.get_or_404(id)

    if task.user_id != session["user_id"]:
        return jsonify(error="Unauthorized"), 403

    task.title = request.form["title"]
    task.description = request.form["description"]
    task.status = request.form["status"]
    db.session.commit()

    return jsonify(success=True)

@tasks_bp.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)

    if task.user_id != session["user_id"]:
        return jsonify(error="Unauthorized"), 403

    db.session.delete(task)
    db.session.commit()
    return jsonify(success=True)
