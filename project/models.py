# API2/project/models.py

from project import db

class ToDoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    city = db.Column(db.String(120), unique=False, nullable=False)
    college = db.Column(db.String(120), unique=False, nullable=False)
    passyear = db.Column(db.Integer, unique=False, nullable=False)
