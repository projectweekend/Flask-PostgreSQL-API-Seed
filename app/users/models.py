from app import db, bcrypt


class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', backref='user', lazy='dynamic')

    def __init__(self, email, password, roles=['regular']):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.active = True
        for r in roles:
            self.roles.append(Role(name=r))

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'active': self.active,
            'roles': [r.name for r in self.roles]
        }


class Role(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    db.UniqueConstraint('user_id', 'name')
