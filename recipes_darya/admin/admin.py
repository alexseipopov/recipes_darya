from flask_admin.contrib.sqla import ModelView

from recipes_darya import db
from recipes_darya.admin import admin
from recipes_darya.modal.model import Dish, Ingredient


class IngredientView(ModelView):
    pass


class DishView(ModelView):
    form_ajax_refs = {
        'ingredients': {
            'fields': (Ingredient.name,)
        }
    }

    form_create_rules = ('name', 'quantity', 'description', 'ingredients')


admin.add_view(IngredientView(Ingredient, db.session, name='Ingredient'))
admin.add_view(DishView(Dish, db.session, name='Dish'))
