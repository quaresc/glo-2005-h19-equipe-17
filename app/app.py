import os
from flask import Flask
from flask_cors import CORS
from controllers import register_controllers

app = Flask("GLO-2005")
CORS(app)
register_controllers(app)

app.run(host=os.environ['IP'], port=os.environ['PORT'])
