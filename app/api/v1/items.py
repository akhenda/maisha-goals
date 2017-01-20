from flask import request
from . import api
from .. import db


@api.route('/bucketlists/<int:id>/items/', methods=['GET'])
def get_items(id):
    pass

@api.route('/bucketlists/<int:id>/items/<int:id>', methods=['GET'])
def get_item(id):
    pass

@api.route('/bucketlists/<int:id>/items/', methods=['POST'])
def new_item(id):
    pass

@api.route('/bucketlists/<int:id>/items/<int:id>', methods=['PUT'])
def edit_item(id):
    pass

@api.route('/bucketlists/<int:id>/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    pass
