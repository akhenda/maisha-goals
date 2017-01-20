from flask import Blueprint

api = Blueprint('api', __name__)


def before_request():
    """All routes in this blueprint require authentication."""
    pass


def after_request(rv):
    """Generate an ETag header for all routes in this blueprint."""
    return rv
