ingredients_put = {
    "tags": "Ingredients",
    "summery": "Update ingredients",
    "description": "Update description",
    "parametres": [
        {
            "name": "data",
            "in": "body",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "protein": {
                        "type": "integer"
                    },
                    "fat": {
                        "type": "integer"
                    },
                    "carb": {
                        "type": "integer"
                    },
                    "calories": {
                        "type": "integer"
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
                            "ingredients": {
                                "id": {
                                    "type": "integer",
                                    "example": 1
                                },
                                "name": {
                                    "type": "string",
                                    "example": "name"
                                },
                                "protein": {
                                    "type": "integer",
                                    "example": 2
                                },
                                "fat": {
                                    "type": "integer",
                                    "example": 3
                                },
                                "carb": {
                                    "type": "integer",
                                    "example": 4
                                },
                                "calories": {
                                    "type": "integer",
                                    "example": 5
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
                        "enum": [2]
                    },
                    "description": {
                        "type": "string",
                        "enum": ["Fail"]
                    },
                    "data": {
                        "type": "object",
                        "properties": {}
                    }
                }
            }
        }
    }
}
