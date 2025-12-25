# user database model

from app.extensions import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default="pending")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
