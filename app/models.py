from . import db


class User(db.Model):
    ''' Users DB interface '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))


class Bucketlist(db.Model):
    ''' Bucketlists DB interface '''
    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.now)
    date_modified = db.Column(db.DateTime,
                              onupdate=datetime.now)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='user', lazy='dynamic')
    items = db.relationship('BucketlistItem', backref='bucketlist',
                            lazy='dynamic',
                            cascade='all, delete-orphan')


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
    user = db.relationship('User', backref'bucketlistItem', lazy='dynamic')
    is_done = db.Column(db.Boolean, default=False)
