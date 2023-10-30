from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@recipes_db:5430/recipes'
app.config["SECRET_KEY"] = "secret key"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Swagger(app)

from recipes_darya.api import api as a

app.register_blueprint(a)

from recipes_darya.admin import admin
