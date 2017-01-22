from flask import g, request
from . import api
from .. import db
from ..models import User
from ..decorators import json, paginate


@api.route('/users/', methods=['GET'])
@json
@paginate('users')
def get_users():
    return User.query


@api.route('/users/<int:id>', methods=['GET'])
@json
def get_user(id):
    return User.query.get_or_404(id)


@api.route('/users/<int:id>', methods=['PUT'])
@json
def edit_user(id):
    user = User.query.get_or_404(id)
    if not request.json:
        return {
            'status': 400,
            'error': 'bad request',
            'message': 'you did not send any data',
        }, 400, {}
    user.import_data(request.json)
    db.session.add(user)
    db.session.commit()
    return {}


@api.route('/users/<int:id>', methods=['DELETE'])
@json
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return {}
