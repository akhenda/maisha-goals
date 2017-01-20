from flask import request
from . import api
from .. import db


@api.route('/bucketlists/', methods=['GET'])
def get_bucketlists():
    pass


@api.route('/bucketlists/<int:id>', methods=['GET'])
def get_bucketlist(id):
    pass


@api.route('/bucketlists/', methods=['POST'])
def new_bucketlist():
    pass


@api.route('/bucketlists/<int:id>', methods=['PUT'])
def edit_bucketlist(id):
    pass


@api.route('/bucketlists/<int:id>', methods=['DELETE'])
def delete_bucketlist(id):
    pass
