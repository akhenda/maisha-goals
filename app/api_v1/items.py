from flask import g, request, abort
from . import api
from .. import db
from ..models import Bucketlist, BucketlistItem
from ..decorators import json, paginate


def check_permissions(id):
    bucketlist = Bucketlist.query.get_or_404(id).export_data()
    if bucketlist['created_by'] != g.user.id:
        abort(403)


@api.route('/bucketlists/<int:id>/items/', methods=['GET'])
@json
@paginate('items')
def get_items(id):
    check_permissions(id)
    bucketlist = Bucketlist.query.get_or_404(id)
    return bucketlist.items


@api.route('/bucketlists/<int:id>/items/', methods=['POST'])
@json
def new_item(id):
    check_permissions(id)
    bucketlist = Bucketlist.query.get_or_404(id)
    item = BucketlistItem(bucketlist=bucketlist)
    if not request.json:
        return {
            'status': 400,
            'error': 'bad request',
            'message': 'you did not send any data',
        }, 400, {}
    request.json['bucketlist_id'] = id
    item.import_data(request.json)
    db.session.add(item)
    db.session.commit()
    return {
        "message": "Bucketlist item successfuly created"
    }, 201, {'Location': item.get_url()}


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['GET'])
@json
def get_item(id, item_id):
    check_permissions(id)
    item = BucketlistItem.query.filter_by(
                                    bucketlist_id=id,
                                    id=item_id
                                ).first_or_404()
    return item.export_data()


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['PUT'])
@json
def edit_item(id, item_id):
    check_permissions(id)
    item = BucketlistItem.query.filter_by(
                                    bucketlist_id=id,
                                    id=item_id
                                ).first_or_404()
    if not request.json:
        return {
            'status': 400,
            'error': 'bad request',
            'message': 'you did not send any data',
        }, 400, {}
    request.json['bucketlist_id'] = id
    item.import_data(request.json)
    db.session.add(item)
    db.session.commit()
    return {"message": "Bucketlist item successfuly updated"}


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['DELETE'])
@json
def delete_item(id, item_id):
    check_permissions(id)
    item = BucketlistItem.query.filter_by(
                                    bucketlist_id=id,
                                    id=item_id
                                ).first_or_404()
    db.session.delete(item)
    db.session.commit()
    return {"message": "Bucketlist item successfuly deleted"}
