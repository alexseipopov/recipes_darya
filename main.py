import sqlalchemy as sa
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


class Ingredient(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False, unique=True)


if __name__ == '__main__':
    app.run(port=5005, debug=True, host='0.0.0.0')
