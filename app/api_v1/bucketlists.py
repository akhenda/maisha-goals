from flask import g, request
from . import api
from .. import db
from ..models import User, Bucketlist
from ..decorators import json, paginate


@api.route('/bucketlists/', methods=['GET'])
@json
@paginate('bucketlists')
def get_bucketlists():
    return Bucketlist.query


@api.route('/bucketlists/<int:id>', methods=['GET'])
@json
def get_bucketlist(id):
    return Bucketlist.query.get_or_404(id)


@api.route('/bucketlists/', methods=['POST'])
@json
def new_bucketlist():
    user = User.query.get_or_404(g.user.id)
    bucketlist = Bucketlist(created_by=user.id)
    bucketlist.import_data(request.json)
    db.session.add(bucketlist)
    db.session.commit()
    return {}, 201, {'Location': bucketlist.get_url()}


@api.route('/bucketlists/<int:id>', methods=['PUT'])
@json
def edit_bucketlist(id):
    bucketlist = Bucketlist.query.get_or_404(id)
    bucketlist.import_data(request.json)
    db.session.add(bucketlist)
    db.session.commit()
    return {}


@api.route('/bucketlists/<int:id>', methods=['DELETE'])
@json
def delete_bucketlist(id):
    bucketlist = Bucketlist.query.get_or_404(id)
    db.session.delete(bucketlist)
    db.session.commit()
    return {}
