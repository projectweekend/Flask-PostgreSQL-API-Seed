from flask import Flask
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('config')

rest_api = restful.Api(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


import routes


db.create_all()
