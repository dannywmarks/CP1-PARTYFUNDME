from flask import Flask, request, render_template, jsonify, Blueprint, url_for, abort
from os import environ
from flask_mail import Mail, Message
from .. import mail
from partyfundme.utils import serializer
from partyfundme.main.forms import EmailForm

mail_blueprint = Blueprint('mail_blueprint', 
                              __name__, 
                              template_folder='templates', 
                              static_folder='static')

@mail_blueprint.route('/send_mail', methods=['POST'])
def send_email():

    form = EmailForm()

    if form.validate_on_submit():
      name = form.name.data
      email = form.email.data
      body = form.body.data



    msg = Message(subject=f"BAR SIGN UP FROM {name}",
                      sender=email,
                      recipients=["dannydamage@me.com"], # replace with your email for testing
                      body=body)
    mail.send(msg)
    return "Email sent"