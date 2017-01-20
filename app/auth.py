from flask import jsonify, g, current_app
from flask_httpauth import HTTPBasicAuth
from .models import User

auth = HTTPBasicAuth()
auth_token = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    pass


@auth.error_handler
def unauthorized():
    pass


@auth_token.verify_password
def verify_auth_token(token, unused):
    pass


@auth_token.error_handler
def unauthorized_token():
    pass
