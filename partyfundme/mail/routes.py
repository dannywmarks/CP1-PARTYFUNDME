from flask import Flask, render_template, redirect, Blueprint, url_for, flash, request, session
from ..models import db
from flask_login import current_user
from os import environ
from flask_mail import Mail, Message
from partyfundme.utils import serializer
from partyfundme.main.forms import EmailForm
from partyfundme import flask_mail
from ..models import Event


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


@mail_blueprint.route('/ticket', methods=['GET','POST'])
def ticket():
    """ Composes and sends an email for the Bar Sign up form with html ticket and appends current user to event"""
    
    name = current_user.username
    email = current_user.email
    event_name = session['current_event_name']
    event_id = session['current_event_id']
    event_date = session['current_event_date']

    event = Event.query.get_or_404(event_id)

    event.rsvps.append(current_user)
    event.total_fund = event.total_fund + 25

    db.session.add(event)
    db.session.commit()

    msg = Message(subject=f"BAR SIGN UP FORM {name}",
                      sender=email,
                      recipients=["dannydamage@me.com"], # replace with your email for testing
                      html=render_template('ticket_email.html', event_name=event_name, event_id=event_id, event_date=event_date))
    flask_mail.send(msg)
    flash('Email Sent! We will be in contact shortly!', 'success')
    return redirect(url_for('payments_blueprint.thanks'))