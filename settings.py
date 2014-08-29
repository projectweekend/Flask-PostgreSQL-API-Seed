import os

DEBUG = os.getenv('DEBUG', False)

PORT = os.getenv('PORT')

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
    'postgres://docker:docker@{0}/docker'.format(os.getenv('DB_1_PORT_5432_TCP_ADDR')))
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = False

SECRET_KEY = os.getenv('SECRET_KEY', None)
assert SECRET_KEY
