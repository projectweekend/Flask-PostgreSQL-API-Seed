from functools import wraps

from flask.ext import restful
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import app, bcrypt


TWO_WEEKS = 1209600


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if True:
            # TODO
            return func(*args, **kwargs)

        restful.abort(401)
    return wrapper


def generate_token(user, expiration=TWO_WEEKS):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps(user.to_dict())
