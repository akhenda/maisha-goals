import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../app/databases/pro.db')

DEBUG = False
SECRET_KEY = '6iHBEgAe4luM2quEtCY5'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + db_path
