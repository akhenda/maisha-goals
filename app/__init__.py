import os
from flask import Flask, jsonify, g
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
    from .models import User

    @app.route('/auth/register')
    @json
    def register_user():
        u = User()
        u.import_data(request.json)
        db.session.add(u)
        db.session.commit()
        return {'message': 'The user has been created successfully'}, 201, {}

    @app.route('/auth/login')
    @auth.login_required
    @json
    def login_user():
        return {'token': g.user.generate_auth_token()}

    return app
