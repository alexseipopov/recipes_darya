from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'
app.config["SECRET_KEY"] = "secret key"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from recipes_darya.api import api as a

app.register_blueprint(a)

from recipes_darya.admin import admin
