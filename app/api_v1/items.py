from flask import g, request
from . import api
from .. import db
from ..models import User, Bucketlist, BucketlistItem
from ..decorators import json, paginate


@api.route('/bucketlists/<int:id>/items/', methods=['GET'])
@json
@paginate('items')
def get_items(id):
    bucketlist = Bucketlist.query.get_or_404(id)
    return bucketlist.items


@api.route('/bucketlists/<int:id>/items/', methods=['POST'])
@json
def new_item(id):
    bucketlist = Bucketlist.query.get_or_404(id)
    item = BucketlistItem(bucketlist=bucketlist)
    request.json['bucketlist_id'] = id
    item.import_data(request.json)
    db.session.add(item)
    db.session.commit()
    return {}, 201, {'Location': item.get_url()}


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['GET'])
@json
def get_item(id, item_id):
    return BucketlistItem.query.get_or_404(id).export_data()


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['PUT'])
@json
def edit_item(id, item_id):
    # we'll handle the accessing unauthorized access here i.e.
    # if id != g.user.id
    # user = User.query.get_or_404(id)
    item = BucketlistItem.query.get_or_404(item_id)
    item.import_data(request.json)
    db.session.add(item)
    db.session.commit()
    return {}


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['DELETE'])
@json
def delete_item(id, item_id):
    item = BucketlistItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return {}
