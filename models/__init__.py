from flask_sqlalchemy import SQLAlchemy
from config import app_activate, app_config
from flask import Flask


config = app_config[app_activate]

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app=app)