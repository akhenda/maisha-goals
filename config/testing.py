import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../app/databases/test.db')

DEBUG = False
TESTING = True
SECRET_KEY = 'SqCgW6kUtw0ypcjfl379'
SERVER_NAME = ''
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_path
