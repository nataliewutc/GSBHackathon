from flask_frozen import Freezer
from myapp import app

freezer = Freezer(app)

if name == 'main':
    freezer.freeze()
