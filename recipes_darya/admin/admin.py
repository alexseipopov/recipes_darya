from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from recipes_darya import app
from ..modal.model import Ingredient, Dish
from recipes_darya import db

admin = Admin(app)


class RecipesIndexView(ModelView):
    pass


admin.add_view(RecipesIndexView(Ingredient, db.session, name='Ingredient'))
admin.add_view(RecipesIndexView(Dish, db.session, name='Dish'))
