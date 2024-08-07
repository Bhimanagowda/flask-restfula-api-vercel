# API2/project/routes.py

from flask import render_template
from project import app
from project.models import ToDoModel

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/display')
def display():
    todos = ToDoModel.query.all()
    return render_template('display.html', todos=todos)
