from flask import Blueprint
from ..auth import auth_token
from .v1 import bucketlists, items, errors


api = Blueprint('api', __name__)


def before_request():
    """All routes in this blueprint require authentication."""
    pass


def after_request(rv):
    """Generate an ETag header for all routes in this blueprint."""
    return rv
