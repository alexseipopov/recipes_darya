dishes_put = {
    "tags": ["Dishes"],
    "summary": "Update of dishes by ID",
    "description": "Update of dishes by ID",
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
