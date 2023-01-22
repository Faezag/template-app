from flask import Flask
from flask_bcrypt import Bcrypt
# 1) import flask object

app = Flask(__name__)
# 2) create new app instance from flask object
app.secret_key = "topsecret"
bcrypt = Bcrypt(app)
