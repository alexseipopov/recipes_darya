import sqlalchemy as sa
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Ingredient(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False, unique=True)
    protein = sa.Column(sa.Integer)
    fat = sa.Column(sa.Integer)
    carb = sa.Column(sa.Integer)
    calories = sa.Column(sa.Integer)
    dishes = db.relationship("Dish", backref="ingredients")


class Dish(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False, unique=True)
    weight_of_portion = sa.Column(sa.Integer, nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    ingredients = db.relationship("Ingredient", secondary="dish_ingredient", backref="dishes")


class DishIngredient(db.Model):
    dish_id = sa.Column(sa.Integer, sa.ForeignKey("dish.id"), primary_key=True)
    ingredient_id = sa.Column(sa.Integer, sa.ForeignKey("ingredient.id"), primary_key=True)


with app.app_context():
    db.create_all()


from api import api as a
app.register_blueprint(a)


if __name__ == '__main__':
    app.run(port=5005, debug=True, host='0.0.0.0')
