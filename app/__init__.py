from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
)

from app import routes
