import os
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from .decorators import json

db = SQLAlchemy()


def create_app(config_name):
    """ Create the usual Flask application instance."""
    app = Flask(__name__)

    # Apply configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    # initialize extensions
    db.init_app(app)

    # register blueprints
    from .api_v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    # register an after request handler
    def after_request(rv):
        headers = getattr(g, 'headers', {})
        rv.headers.extend(headers)
        return rv

    # authentication token route
    from .auth import auth

    @app.route('/auth/register')
    @json
    def register_user():
        pass

    @app.route('/auth/login')
    @auth.login_required
    @json
    def get_auth_token():
        return {'token': g.user.generate_auth_token()}

    return app
