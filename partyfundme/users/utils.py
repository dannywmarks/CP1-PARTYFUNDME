from itsdangerous import URLSafeTimedSerializer
from os import environ

#SERIALIZE TOKEN FOR FLASK MAIL CONFIRMATION
serializer = URLSafeTimedSerializer(environ.get('SECRET_KEY'))