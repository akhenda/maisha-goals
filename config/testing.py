import os

basedir = os.path.abspath('.')
os.chdir(basedir)
# db_path = (basedir + '/app/databases/test.db').strip('/')


DEBUG = False
TESTING = True
SECRET_KEY = 'SqCgW6kUtw0ypcjfl379'
SERVER_NAME = 'maisha-goals.com'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.getcwd() + '/app/databases/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
