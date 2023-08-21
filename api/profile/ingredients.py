from .. import api
from main import Ingredient

# CRUD C-reate R-ead U-pdate D-elete


@api.get("/")
def get_api():
    return "API"



