from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with


class UserAPI(restful.Resource):

    def get(self):
        return "Hi"
