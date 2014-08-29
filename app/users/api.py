from flask.ext import restful
from flask.ext.restful import reqparse, fields, marshal_with
from flask_security.core import current_user
from sqlalchemy.exc import IntegrityError


from app.users.models import user_datastore
from app.utils.auth import auth_required
from app.utils.errors import EMAIL_IN_USE
from app import db


class UserAPI(restful.Resource):

    reg_parser = reqparse.RequestParser()
    reg_parser.add_argument('email', type=str, required=True)
    reg_parser.add_argument('password', type=str, required=True)

    user_fields = {
        'id': fields.Integer,
        'email': fields.String,
    }

    @marshal_with(user_fields)
    @auth_required
    def get(self):
        return current_user

    def post(self):
        args = self.reg_parser.parse_args()

        user = user_datastore.create_user(email=args['email'], password=args['password'])
        try:
            db.session.commit()
        except IntegrityError:
            return EMAIL_IN_USE

        return {
            'id': user.id,
            'token': user.get_auth_token()
        }, 201
