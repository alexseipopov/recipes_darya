from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from recipes_darya.api import api as a
app.register_blueprint(a)
