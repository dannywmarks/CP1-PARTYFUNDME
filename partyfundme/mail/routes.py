from flask import Flask, render_template, redirect, Blueprint, url_for, flash
from ..models import db
from flask_login import current_user
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



    msg = Message(subject=f"BAR SIGN UP FORM {name}",
                      sender=email,
                      recipients=["dannydamage@me.com"], # replace with your email for testing
                      body=body)
    mail.send(msg)
    return "Email sent"


@mail_blueprint.route('/mailing_list', methods=['POST'])
def mailing_list():

  user = current_user
  
  if form.validate_on_submit():

    if user:
      user.mailing_list = True

      db.session.commit()
      flash('Your account has been updated!', 'success')
      return redirect(url_for('main.home'))
