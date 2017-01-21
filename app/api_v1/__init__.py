from flask import Blueprint
from ..auth import auth_token
api = Blueprint('api', __name__)
from . import bucketlists, items, errors


@api.before_request
def before_request():
    """ All routes in this blueprint require authentication. """
    pass


@api.after_request
def after_request(rv):
    """ All after request operations will be handled here """
    return rv
