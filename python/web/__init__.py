from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ALLOWED_EXTENSIONS = set(['json'])

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from web import views