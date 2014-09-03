from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('settings')

rest_api = restful.Api(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


import urls


db.create_all()
