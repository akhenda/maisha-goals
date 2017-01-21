from datetime import datetime
from dateutil import parser as datetime_parser
from dateutil.tz import tzutc
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import url_for, current_app
from . import db
from .exceptions import ValidationError
from .utils import split_url


class User(db.Model):
    ''' Users DB interface '''
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def import_data(self, data):
        try:
            if not self.query.filter_by(username=data['username']).count():
                self.username = data['username']
                self.password_hash = generate_password_hash(data['password'])
            else:
                raise ValidationError('That username is taken.')
        except KeyError as e:
            raise ValidationError('Invalid user: missing ' + e.args[0])
        return self


class Bucketlist(db.Model):
    ''' Bucketlists DB interface '''
    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.now)
    date_modified = db.Column(db.DateTime,
                              onupdate=datetime.now)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    # user = db.relationship('User',
    #                        backref=db.backref('bucketlist', lazy="dynamic"))
    items = db.relationship('BucketlistItem', backref='bucketlist',
                            lazy='dynamic',
                            cascade='all, delete-orphan')

    def get_url(self):
        return url_for('api.get_bucketlist', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'name': self.name,
            'description': self.description,
            'items_url': url_for('api.get_bucketlists', id=self.id,
                                 _external=True)
        }

    def import_data(self, data):
        try:
            if not self.query.filter_by(name=data['name']).count():
                self.name = data['name']
            else:
                raise ValidationError('You already have a bucketlist \
                    with that name.')
        except KeyError as e:
            raise ValidationError('Invalid bucketlist: missing ' + e.args[0])
        return self


class BucketlistItem(db.Model):
    ''' Bucketlist Items DB interface '''
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text)
    bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucketlists.id'))
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    date_created = db.Column(db.DateTime, default=datetime.now)
    date_modified = db.Column(db.DateTime,
                              onupdate=datetime.now)
    user = db.relationship('User',
                           backref=db.backref('bucketlistitems',
                                              lazy='dynamic'))
    is_done = db.Column(db.Boolean, default=False)

    def get_url(self):
        return url_for('api.get_item', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'bucketlist_url': self.bucketlist.get_url(),
            'name': self.name
        }

    def import_data(self, data):
        try:
            endpoint, args = split_url(data['bucketlist_url'])
            self.name = data['name']
            self.description = data['description']
        except KeyError as e:
            raise ValidationError('Invalid item: missing ' + e.args[0])
        if endpoint != 'api.get_bucketlist' or not 'id' in args:
            raise ValidationError('Invalid bucketlist URL: ' +
                                  data['bucketlist_url'])
        self.bucketlist = Bucketlist.query.get(args['id'])
        if self.bucketlist is None:
            raise ValidationError('Invalid bucketlist URL: ' +
                                  data['bucketlist_url'])
        return self
