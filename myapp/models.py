from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1

db = SQLAlchemy()
lm = LoginManager()

def get_or_create(db, model, **kwargs):
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        return instance

########################################################################
class Things(db.Model):
    """"""
    __tablename__ = "things"

    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String)


    def __init__(self, name):
        """"""
        self.name = name.lower()

    def __repr__(self):
        if self.id:
            return '<Thing#%d: %s>' % (self.id, self.name)
        return '<Thing: %s>' % (self.name)

########################################################################
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    pw_hash = db.Column(db.String(120))



    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def is_authenticated(self):
        """Should return True unless the object represents a user that should not be allowed to authenticate for some reason. """
        return True

    def is_active(self):
        """should return True for users unless they are inactive (e.g. they've been banned)"""
        return True

    def is_anonymous(self):
        """should return True only for fake users that are not supposed to log in to the system."""
        return False

    def get_id(self):
        """should return a unique identifier for user, in unicode format. """
        return unicode(self.id)

    def __init__(self, name, password):
        """"""
        self.name = name
        self.pw_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % (self.name)

