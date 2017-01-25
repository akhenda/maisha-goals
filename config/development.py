import os

basedir = os.path.abspath('../')
db_path = os.path.join(basedir, 'app/databases/dev.db')

DEBUG = True
IGNORE_AUTH = True
SECRET_KEY = 'wzQcp820vrYFE46bj3yL'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + db_path
SQLALCHEMY_TRACK_MODIFICATIONS = True
