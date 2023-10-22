ingredients_get = {
    "tags": ["Ingredients"],
    "summary": "Get all ingredients",
    "description": "Get all ingredients",
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
                            "ingredient": {
                                "type": "array",
                                "items": {
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
                }
            }
        }
    }
}
