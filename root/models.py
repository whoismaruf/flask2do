from root import db

class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    task = db.Column(db.String(120), unique=True)