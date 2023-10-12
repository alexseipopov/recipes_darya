ingredients_delete = {
    "tags": "Ingredients",
    "summary": "Delete ingredients",
    "description": "Delete ingredients",
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
                    "data": {}
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
                    "data": {}
                }
            }
        }
    }
}
