from flask import Blueprint
from ..auth import auth_token


api = Blueprint('api', __name__)

from . import bucketlists, items, errors, users


@api.before_request
@auth_token.login_required
def before_request():
    """ All API routes require authentication. """
    pass


@api.after_request
def after_request(rv):
    """ All after request operations will be handled here """
    return rv
