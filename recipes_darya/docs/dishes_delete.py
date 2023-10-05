dishes_delete = {
    "tags": ["Dishes"],
    "summary": "Delete dishes by ID",
    "description": "Delete dishes by ID",
    "operationId": "deleteDishesById",
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
