from flask.ext import restful
from flask.ext.restful import fields, marshal_with
from sqlalchemy.exc import IntegrityError


from app.users.mixins import SignupLoginMixin
from app.users.models import User

from app.utils.auth import auth_required, generate_token
from app.utils.errors import EMAIL_IN_USE

from app import db


user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'password': fields.String
}


class UserAPI(SignupLoginMixin, restful.Resource):

    @marshal_with(user_fields)
    @auth_required
    def get(self):
        return {}, 200

    def post(self):
        args = self.reg_parser.parse_args()

        user = User(email=args['email'], password=args['password'])
        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            return EMAIL_IN_USE

        return {
            'id': user.id,
            'token': generate_token(user)
        }, 201



class AuthenticationAPI(restful.Resource):

    def post(self):
        args = self.reg_parser.parse_args()

        return {}, 200

