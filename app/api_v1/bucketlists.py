from flask import g, request
from . import api
from .. import db
from ..models import User, Bucketlist
from ..decorators import json, paginate


@api.route('/bucketlists/', methods=['GET'])
@json
@paginate('bucketlists')
def get_bucketlists():
    if request.args.get('q'):
        return Bucketlist.query.filter_by(created_by=g.user.id, name=request.args.get('q'))
    return Bucketlist.query.filter_by(created_by=g.user.id)


@api.route('/bucketlists/<int:id>', methods=['GET'])
@json
def get_bucketlist(id):
    return Bucketlist.query.get_or_404(id)


@api.route('/bucketlists/', methods=['POST'])
@json
def new_bucketlist():
    user = User.query.get_or_404(g.user.id)
    bucketlist = Bucketlist(created_by=user.id)
    if not request.json:
        return {
            'status': 400,
            'error': 'bad request',
            'message': 'you did not send any data',
        }, 400, {}
    bucketlist.import_data(request.json)
    db.session.add(bucketlist)
    db.session.commit()
    return {
        "message": "Bucketlist successfuly created"
    }, 201, {'Location': bucketlist.get_url()}


@api.route('/bucketlists/<int:id>', methods=['PUT'])
@json
def edit_bucketlist(id):
    bucketlist = Bucketlist.query.get_or_404(id)
    if not request.json:
        return {
            'status': 400,
            'error': 'bad request',
            'message': 'you did not send any data',
        }, 400, {}
    bucketlist.import_data(request.json)
    db.session.add(bucketlist)
    db.session.commit()
    return {"message": "Bucketlist successfuly updated"}


@api.route('/bucketlists/<int:id>', methods=['DELETE'])
@json
def delete_bucketlist(id):
    bucketlist = Bucketlist.query.get_or_404(id)
    db.session.delete(bucketlist)
    db.session.commit()
    return {"message": "Bucketlist successfuly deleted"}
