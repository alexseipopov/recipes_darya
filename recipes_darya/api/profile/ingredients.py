from flask import request
from flasgger import swag_from

from recipes_darya import db
from recipes_darya.modal.model import Ingredient

from .. import api
from recipes_darya.docs import ingredients_get, ingredients_post, ingredients_put, ingredients_delete

# CRUD C-reate R-ead U-pdate D-elete


@api.get("/ingredients")
@swag_from(ingredients_get)
def get_all_ingredients():
    ingredients = Ingredient.query.all()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "ingredients": [{
                "id": item.id,
                "name": item.name,
                "protein": item.protein,
                "fat": item.fat,
                "carb": item.carb,
                "calories": item.calories
            } for item in ingredients]
        }
    }, 200


@api.post("/ingredients")
@swag_from(ingredients_post)
def new_ingredients():
    name = request.json.get("name")
    protein = request.json.get("protein")
    fat = request.json.get("fat")
    carb = request.json.get("carb")
    calories = request.json.get("calories")
    if not name:
        return {
            "status": 1,
            "description": "Fail",
            "data": {}
        }, 400
    check_name = Ingredient.query.filter_by(name=name).first()
    if check_name:
        return {
            "status": 1,
            "description": "Name already exist",
            "data": {}
        }, 400
    item = Ingredient(name=name, protein=protein, fat=fat, carb=carb, calories=calories)
    db.session.add(item)
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "ingredients": {
                "id": item.id,
                "name": item.name,
                "protein": item.protein,
                "fat": item.fat,
                "carb": item.carb,
                "calories": item.calories
            }
        }
    }, 200


@api.put("/ingredients/<int:id>")
@swag_from(ingredients_put)
def update_ingredients(id):
    item = Ingredient.query.get(id)
    if not item:
        return {
            "status": 2,
            "description": "Fail",
            "data": {}
        }, 400
    name = request.json.get("name")
    protein = request.json.get("protein")
    fat = request.json.get("fat")
    carb = request.json.get("carb")
    calories = request.json.get("calories")
    item.name = name if name else item.name
    item.protein = protein if protein else item.protein
    item.fat = fat if fat else item.fat
    item.carb = carb if carb else item.carb
    item.calories = calories if calories else item.calories
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "ingredients": {
                "id": item.id,
                "name": item.name,
                "protein": item.protein,
                "fat": item.fat,
                "carb": item.carb,
                "calories": item.calories
            }
        }
    }, 200


@api.delete("/ingredients/<int:id>")
@swag_from(ingredients_delete)
def delete_ingredients(id):
    item = Ingredient.query.get(id)
    if not item:
        return {
            "status": 2,
            "description": "Fail",
            "data": {}
        }, 400
    db.session.delete(item)
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "ingredients": {
                "id": item.id,
                "name": item.name,
                "protein": item.protein,
                "fat": item.fat,
                "carb": item.carb,
                "calories": item.calories
            }
        }
    }, 200
