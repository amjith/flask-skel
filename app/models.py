from hashlib import md5
import flask.ext.whooshalchemy as whooshalchemy
from app import db, app

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime())

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def avatar(self, size):
        return ('http://www.gravatar.com/avatar/%s?d=retro&s=%d' %
                (md5(self.email).hexdigest(), size))

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        version = 1
        while True:
            new_nickname = 'nickname%d' % version
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            version += 1
        return new_nickname

class Item(db.Model):
    __searchable__ = ['body']

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return 'Body: %s' % (self.body)

whooshalchemy.whoosh_index(app, Item)
