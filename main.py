import sqlalchemy as sa
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


class Ingredient(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False, unique=True)
    protein = sa.Column(sa.Integer)
    fat = sa.Column(sa.Integer)
    carb = sa.Column(sa.Integer)
    calories = sa.Column(sa.Integer)


if __name__ == '__main__':
    app.run(port=5005, debug=True, host='0.0.0.0')
