from itsdangerous import URLSafeTimedSerializer
from partyfundme import app
from os import environ
import secrets
import os


#SERIALIZE TOKEN FOR FLASK MAIL CONFIRMATION
serializer = URLSafeTimedSerializer(environ.get('SECRET_KEY'))

#RANDOM FILE NAME GENERATOR TO PREVENT COLISION
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


    