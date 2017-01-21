from flask import jsonify
from ..exceptions import ValidationError
from . import api


@api.errorhandler(ValidationError)
def bad_request(e):
    res = jsonify({'status': 400, 'error': 'bad request',
                  'message': e.args[0]})
    res.status_code = 400
    return res


@api.app_errorhandler(404)
def not_found(e):
    res = jsonify({'status': 404, 'error': 'not found',
                  'message': 'invalid resource URL'})
    res.status_code = 404
    return res


@api.errorhandler(405)
def method_not_supported(e):
    res = jsonify({'status': 405, 'error': 'method not supported',
                  'message': 'the method is not supported'})
    res.status_code = 405
    return res


@api.app_errorhandler(500)
def internal_server_error(e):
    res = jsonify({'status': 500, 'error': 'internal server error',
                  'message': e.args[0]})
    res.status_code = 500
    return res
