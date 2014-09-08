from datetime import datetime

from app import db, bcrypt
from app.utils.misc import make_code


class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean())

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.active = True
        self.is_admin = is_admin

    def deactivate(self):
        self.active = False


class PasswordReset(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.Integer(), db.ForeignKey('user.id'))
    code = db.Column(db.String(255), unique=True, default=make_code)
    date = db.Column(db.DateTime(), default=datetime.now)

    db.UniqueConstraint('user', 'code', name='uni_user_code')
