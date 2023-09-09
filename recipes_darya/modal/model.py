import sqlalchemy as sa

from recipes_darya import db


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
    quantity = sa.Column(sa.Integer, nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    ingredients = db.relationship("Ingredient", secondary="dish_ingredient", backref="dishes")


class DishIngredient(db.Model):
    dish_id = sa.Column(sa.Integer, sa.ForeignKey("dish.id"), primary_key=True)
    ingredient_id = sa.Column(sa.Integer, sa.ForeignKey("ingredient.id"), primary_key=True)
