from flask import g, request
from . import api
from .. import db
from ..models import User, Bucketlist, BucketlistItem
from ..decorators import json, paginate


@api.route('/bucketlists/', methods=['GET'])
@json
@paginate('bucketlists')
def get_bucketlists():
    return Bucketlist.query


@api.route('/bucketlists/<int:id>', methods=['GET'])
def get_bucketlist(id):
    return Bucketlist.query.get_or_404(id)


@api.route('/bucketlists/', methods=['POST'])
def new_bucketlist():
    user = User.query.get_or_404(g.user.id)
    bucketlist = Bucketlist(user=user)
    bucketlist.import_data(request.json)
    db.session.add(bucketlist)
    db.session.commit()
    return {}, 201, {'Location': bucketlist.get_url()}


@api.route('/bucketlists/<int:id>', methods=['PUT'])
def edit_bucketlist(id):
    pass


@api.route('/bucketlists/<int:id>', methods=['DELETE'])
def delete_bucketlist(id):
    pass
