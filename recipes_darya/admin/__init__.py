from flask_admin import Admin

from recipes_darya import app

admin = Admin(app)

import recipes_darya.admin.admin
