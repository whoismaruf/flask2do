from root import db
from flask_login import UserMixin


class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    task = db.Column(db.Text(260), nullable=False)
    tasker_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return [self.task, self.tasker_id]


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    tasks = db.relationship('Todo', backref='tasker', lazy=True)

    def __str__(self):
        return [self.username, self.email]
