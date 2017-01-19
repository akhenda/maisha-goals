import os
from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    """ Create the usual Flask application instance."""
    app = Flask(__name__)

    # Apply configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    return app
