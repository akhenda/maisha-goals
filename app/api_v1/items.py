from flask import request
from . import api
from .. import db
from ..models import BucketlistItem


@api.route('/bucketlists/<int:id>/items/', methods=['GET'])
def get_items(id):
    pass


@api.route('/bucketlists/<int:id>/items/', methods=['POST'])
def new_item(id):
    pass


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['GET'])
def get_item(id, item_id):
    pass


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['PUT'])
def edit_item(id, item_id):
    pass


@api.route('/bucketlists/<int:id>/items/<int:item_id>', methods=['DELETE'])
def delete_item(id, item_id):
    pass
