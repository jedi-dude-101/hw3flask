from flask import Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))

myobj = Flask(__name__)

myobj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
)

from app import routes
