from flask import request
from flasgger import swag_from

from recipes_darya import db
from recipes_darya.modal.model import Dish

from .. import api
from recipes_darya.docs import dishes_get


@api.get("/dishes")
@swag_from(dishes_get)
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
@swag_from({
    "tags": ["Dishes"],
    "summary": "Create new dish",
    "description": "Create new dish",
    "parameters": [
        {
            "name": "data",
            "in": "body",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "quantity": {
                        "type": "integer"
                    },
                    "description": {
                        "type": "string"
                    }
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "OK",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "integer",
                        "enum": [0]
                    },
                    "description": {
                        "type": "string",
                        "enum": ["OK"]
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "dishes": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "example": 1
                                    },
                                    "name": {
                                        "type": "string",
                                        "example": "name"
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "example": 1
                                    },
                                    "description": {
                                        "type": "string",
                                        "example": "description"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "400": {
            "description": "Fail description",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "integer",
                        "enum": [1]
                    },
                    "description": {
                        "type": "string",
                        "enum": ["Fail", "Name already exist"]
                    },
                    "data": {
                        "type": "object",
                        "properties": {}
                    }
                }
            }
        }
    }
})
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
