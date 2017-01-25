import os

basedir = os.path.abspath('.')
# db_path = os.path.join(basedir, '/app/databases/test.db')


DEBUG = False
TESTING = True
SECRET_KEY = 'SqCgW6kUtw0ypcjfl379'
SERVER_NAME = 'maisha-goals.com'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/app/databases/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
