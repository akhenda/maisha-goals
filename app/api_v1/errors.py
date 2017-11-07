from flask import jsonify
from ..exceptions import ValidationError, ConflictError
from . import api


@api.app_errorhandler(ValidationError)
def generic_bad_request(e):
    res = jsonify({'status': 400, 'error': 'bad request',
                  'message': e.args[0]})
    res.status_code = 400
    return res


@api.app_errorhandler(400)
def bad_request(e):
    res = jsonify({'status': 400, 'error': 'bad request',
                  'message': 'you have sent a malformed request'})
    res.status_code = 400
    return res


@api.app_errorhandler(403)
def forbidden(e):
    res = jsonify({'status': 403, 'error': 'forbidden',
                  'message': 'you do not have the permission to access '
                   'the requested resource'})
    res.status_code = 403
    return res


@api.app_errorhandler(404)
def not_found(e):
    res = jsonify({'status': 404, 'error': 'not found',
                  'message': 'invalid resource URL'})
    res.status_code = 404
    return res


@api.app_errorhandler(405)
def method_not_supported(e):
    res = jsonify({'status': 405, 'error': 'method not supported',
                  'message': 'the method is not supported'})
    res.status_code = 405
    return res


@api.app_errorhandler(ConflictError)
def resource_conflict(e):
    res = jsonify({'status': 409, 'error': 'conflict',
                  'message': e.args[0]})
    res.status_code = 409
    return res


@api.app_errorhandler(500)
def internal_server_error(e):
    res = jsonify({'status': 500, 'error': 'internal server error',
                  'message': e.args[0]})
    res.status_code = 500
    return res
