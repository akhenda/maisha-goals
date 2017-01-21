from flask import request
from . import api
from .. import db
from ..models import BUcketlist, BucketlistItem
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
    pass


@api.route('/bucketlists/<int:id>', methods=['PUT'])
def edit_bucketlist(id):
    pass


@api.route('/bucketlists/<int:id>', methods=['DELETE'])
def delete_bucketlist(id):
    pass
