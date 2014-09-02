from flask.ext.restful import reqparse, fields


class SignupLoginMixin(object):

    reg_parser = reqparse.RequestParser()
    reg_parser.add_argument('email', type=str, required=True)
    reg_parser.add_argument('password', type=str, required=True)
