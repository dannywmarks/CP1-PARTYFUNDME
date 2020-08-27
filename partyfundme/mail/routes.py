from flask import Flask, render_template, redirect, Blueprint, url_for, flash, request
from ..models import db
from flask_login import current_user
from os import environ
from flask_mail import Mail, Message
from partyfundme.utils import serializer
from partyfundme.main.forms import EmailForm
from partyfundme import flask_mail


mail_blueprint = Blueprint('mail_blueprint', 
                              __name__, 
                              template_folder='templates', 
                              static_folder='static')

# Bar Sign up form on main page
@mail_blueprint.route('/send_mail', methods=['POST'])
def send_email():
    """ Composes and sends an email for the Bar Sign up form"""
    
    name = request.form["name"] 
    email = request.form["email"]
    body = request.form["textarea"]
    



    msg = Message(subject=f"BAR SIGN UP FORM {name}",
                      sender=email,
                      recipients=["dannydamage@me.com"], # replace with your email for testing
                      body=body)
    flask_mail.send(msg)
    flash('Email Sent! We will be in contact shortly!', 'success')
    return redirect(url_for('main.home'))

#Mailing list on main page
@mail_blueprint.route('/mailing_list', methods=['POST'])
def mailing_list():
  """ Subscribes user to mailing list """
  user = current_user
  
  # email = request.form["email"]
  

  if user:
    user.mailing_list = True

    db.session.commit()
    flash('You are signed up for mailing list! You can unsubscribe in profile', 'success')
    return redirect(url_for('main.home'))
  
  else:
    flash('Please create an account')
    return redirect(url_for('users.signup'))

@mail_blueprint.route('/unsubscribe', methods=['POST'])
def unsubscribe():
  """ Unubscribes user to mailing list """
  user = current_user
  
  # email = request.form["email"]
  

  if user:
    user.mailing_list = False

    db.session.commit()
    flash('You are unsubcribed from our mailing list!', 'success')
    return redirect(url_for('main.home'))


@mail_blueprint.route('/send_ticket', methods=['POST'])
def send_ticket():
    """ Composes and sends an email for the Bar Sign up form"""
    
    name = request.form["name"] 
    email = request.form["email"]
    



    msg = Message(subject=f"BAR SIGN UP FORM {name}",
                      sender=email,
                      recipients=["dannydamage@me.com"], # replace with your email for testing
                      html=render_template('ticket_email.html'))
    flask_mail.send(msg)
    flash('Email Sent! We will be in contact shortly!', 'success')
    return redirect(url_for('main.home'))