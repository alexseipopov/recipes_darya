from flask import request

from recipes_darya import db
from recipes_darya.modal.model import Dish

from .. import api


@api.get("/dishes")
def get_all_dishes():
    dishes = Dish.query.all()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "dishes": [{
                "id": item.id,
                "name": item.name,
                "quantity": item.quantity,
                "description": item.description
            } for item in dishes]
        }
    }, 200


@api.post("/dishes")
def new_dishes():
    name = request.json.get("name")
    quantity = request.json.get("quantity")
    description = request.json.get("description")
    if not name or not quantity or not description:
        return {
            "status": 1,
            "description": "Fail",
            "data": {}
        }, 400
    check_name = Dish.query.filter_by(name=name).first()
    if check_name:
        return {
            "status": 1,
            "description": "Name already exist",
            "data": {}
        }, 400
    item = Dish(name=name, quantity=quantity, description=description)
    db.session.add(item)
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "dishes": {
                "id": item.id,
                "name": item.name,
                "quantity": item.quantity,
                'description': item.description
            }
        }
    }, 200


@api.put("/dishes/<int:id>")
def update_dishes(id):
    item = Dish.query.get(id)
    if not item:
        return {
            "status": 2,
            "description": "Fail",
            "data": {}
        }, 400
    name = request.json.get("name")
    quantity = request.json.get("quantity")
    description = request.json.get("description")
    item.name = name if name else item.name
    item.quantity = quantity if quantity else item.quantity
    item.description = description if description else item.description
    db.session.commit()
    return {
        "status": 0,
        "description": "OK",
        "data": {
            "dishes": {
                "id": item.id,
                "name": item.name,
                "quantity": item.quantity,
                'description': item.description
            }
        }
    }, 200


@api.delete("/dishes/<int:id>")
def delete_dishes(id):
    item = Dish.query.get(id)
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
            "dishes": {
                "id": item.id,
                "name": item.name,
                "quantity": item.quantity,
                'description': item.description
            }
        }
    }, 200
