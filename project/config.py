# API2/project/config.py
import os

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY',os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 