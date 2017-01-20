from flask import jsonify
from ..exceptions import ValidationError
from . import api


@api.errorhandler(ValidationError)
def bad_request(e):
    pass


@api.app_errorhandler(404)
def not_found(e):
    pass


@api.errorhandler(405)
def method_not_supported(e):
    pass


@api.app_errorhandler(500)
def internal_server_error(e):
    pass
