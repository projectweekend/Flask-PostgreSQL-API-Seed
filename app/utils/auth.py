from flask.ext import restful
from flask_security.decorators import _check_token


from functools import wraps


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if _check_token():
            return func(*args, **kwargs)

        restful.abort(401)
    return wrapper
