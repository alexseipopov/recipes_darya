import sqlalchemy as sa

from recipes_darya import db

dish_ingredient = db.Table(
    "dish_ingredient",
    sa.Column("dish_id", sa.Integer, sa.ForeignKey("dish.id")),
    sa.Column("ingredient_id", sa.Integer, sa.ForeignKey("ingredient.id"))
)


class Ingredient(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False, unique=True)
    protein = sa.Column(sa.Integer)
    fat = sa.Column(sa.Integer)
    carb = sa.Column(sa.Integer)
    calories = sa.Column(sa.Integer)

    def __repr__(self):
        return f"{self.name} [id: {self.id}]"


class Dish(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False, unique=True)
    quantity = sa.Column(sa.Integer, nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    ingredients = db.relationship("Ingredient",
                                  secondary=dish_ingredient,
                                  backref="dishes")
