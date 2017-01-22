import os
from flask import Flask, request, g
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

    # authentication token route
    from .auth import auth
    from .models import User

    @app.route('/api/v1', methods=['GET'])
    @json
    def api_index():
        return {
            "message": "Welcome to Maisha Goals. Register a new "
            " user or login to get started"}

    @app.route('/auth/register', methods=['POST'])
    @json
    def register_user():
        u = User()
        u.import_data(request.json)
        db.session.add(u)
        db.session.commit()
        return {
            'message': 'Your account has been successfuly created'
        }, 201, {'Location': u.get_url()}

    @app.route('/auth/login')
    @auth.login_required
    @json
    def login_user():
        return {'token': g.user.generate_auth_token()}

    return app
