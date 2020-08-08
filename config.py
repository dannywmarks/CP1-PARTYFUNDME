from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """ Set Flask config variables """

    FLASK_APP = 'run.py'
    FLASK_ENV = 'development'
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG = True

    # FLASK MAIL
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME= environ.get('EMAIL_USER')
    MAIL_PASSWORD= environ.get('EMAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL: False

    # STATIC-ASSETS

    # DATABASE
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # STRIPE API KEYS
    STRIPE_PUBLIC_KEY = environ.get('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = environ.get('STRIPE_SECRET_KEY')

    # PRODUCTION KEYS


