dishes_get = {
    "tags": ["Dishes"],
    "summary": "Get all dishes (summary)",
    "description": "Get all dishes (description)",
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
            }
        }
    }
}
