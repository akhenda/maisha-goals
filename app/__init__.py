import os
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

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
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    # register an after request handler
    def after_request(rv):
        headers = getattr(g, 'headers', {})
        rv.headers.extend(headers)
        return rv

    return app
