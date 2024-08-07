# API2/project/__init__.py

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates', static_folder='../static')
api = Api(app)

app.config.from_object('project.config.Config')

db = SQLAlchemy(app)

from project import routes, resources
