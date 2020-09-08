from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """ Set Flask config variables """

    FLASK_APP = 'run.py'
    SECRET_KEY = environ.get('SECRET_KEY')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    # WTF_CSRF_ENABLED = False

    # FLASK MAIL
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME= environ.get('EMAIL_USER')
    MAIL_PASSWORD= environ.get('EMAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL: False

    # PRODUCTION DATABASE
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # FLASK-ASSETS

    # STATIC-ASSETS
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    

    

    # PRODUCTION KEYS




class ProdConfig(Config):
    pass
    
class DevConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

    # DEVELOPMENT DATABASE
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # STRIPE API KEYS
    STRIPE_PUBLIC_KEY = environ.get('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = environ.get('STRIPE_SECRET_KEY')

class TestConfig(Config):
  
    TESTING = True
    WTF_CSRF_ENABLED = False
    SESSION_COOKIE_SECURE = False
    

    # TESTING DATABASE
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI_TEST')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # STRIPE API TEST KEYS
    STRIPE_PUBLIC_KEY = environ.get('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = environ.get('STRIPE_SECRET_KEY')