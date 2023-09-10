from recipes_darya.admin import admin
from flask_admin.contrib.sqla import ModelView
from recipes_darya.modal.model import Ingredient, Dish
from recipes_darya import db


class RecipesIndexView(ModelView):
    pass


admin.add_view(RecipesIndexView(Ingredient, db.session, name='Ingredient'))
admin.add_view(RecipesIndexView(Dish, db.session, name='Dish'))
