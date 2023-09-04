from .. import api
from ...main import db, Ingredient
from flask import request

# CRUD C-reate R-ead U-pdate D-elete


@api.get("/ingredients")
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
def new_ingredient():
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
    item = Ingredient(name=name, protein=protein, fat=fat, carb=carb, calories=calories)
    db.session.add(item)
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "ingredient": {
                "id": item.id,
                "name": item.name,
                "protein": item.protein,
                "fat": item.fat,
                "carb": item.carb,
                "calories": item.calories
            }
        }
    }, 200


@api.put("/ingredient/<int:id>")
def update_ingredient(id):
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
            "ingredient": {
                "id": item.id,
                "name": item.name,
                "protein": item.protein,
                "fat": item.fat,
                "carb": item.carb,
                "calories": item.calories
            }
        }
    }, 200


@api.delete("/ingredient/<int:id>")
def delete_ingredient(id):
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
            "ingredient": {
                "id": item.id,
                "name": item.name,
                "protein": item.protein,
                "fat": item.fat,
                "carb": item.carb,
                "calories": item.calories
            }
        }
    }, 200
