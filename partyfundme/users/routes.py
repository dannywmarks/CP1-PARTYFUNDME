# pylint: disable=E1101
from flask import render_template, Blueprint, redirect, request, url_for, flash, abort, session
from .forms import LoginForm, SignupForm
from ..models import db, User
from itsdangerous import SignatureExpired
from flask_mail import Message
from flask_login import login_required, logout_user, current_user, login_user
from .. import mail
from .utils import serializer
import requests, json


users = Blueprint('users', __name__, template_folder='templates', static_folder='static')



@users.route("/signup", methods=['GET', 'POST'])
def signup():
    """ Registers a User and adds to database then sends a confirmation Email """

    form = SignupForm()
    
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
        
            name = form.name.data
            email = form.email.data
            username = form.username.data
            password = form.password.data

            # Flask-Mail Create Confirmation Email 
            token = serializer.dumps(email, salt='email-confirm')
            msg = Message(subject='Confirm Email', sender='dannywmarks@gmail.com', recipients=[email])
            link = url_for('users.confirm_email', token=token, _external=True)
            msg.body = 'Your Link is {}'.format(link)

            # Send Confirmation Email
            mail.send(msg)

            # Instantiate User
            user = User.register(name, email, username, password)
       
            # Add User to Database
            db.session.add(user)
            db.session.commit()

            flash('User created!')
            return redirect(url_for('main/main.home'))

        flash('User Exists!')
    return render_template('users/signup.html', form=form)


#Confirm users email address with Flask-Mail
@users.route('/confirm/<token>')
def confirm_email(token):
    """ User signup confirmation using token generated on User Signup """ 
    try:  
        email = serializer.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        abort(404)

    # Find user by email
    user = User.query.filter_by(email=email).first_or_404()
    # Turn Email_Confirmed to True
    user.email_confirmed = True

    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('users.login'))



@users.route("/login", methods=['GET', 'POST'])
def login():
    """ Login user. Authorize routes."""
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.authenticate(email, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.home'))
        flash('Invalid username/password combination')
        return redirect(url_for('users.login'))
    
    return render_template("users/signin.html", form=form)



@users.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('users.login'))




# @users.route("/test")
# def email_test():

#     msg = Message(subject="Hello",
#                       sender='dannywmarks@gmail.com',
#                       recipients=["dannydamage@me.com"], # replace with your email for testing
#                       body="This is a test email I sent with Gmail and Python!")
#     mail.send(msg)
#     return "Email sent"

