# pylint: disable=E1101
from flask import render_template, Blueprint, redirect, request, url_for, flash, abort, session
from .forms import LoginForm, SignupForm, UpdateAccountForm
from ..models import db, User
from partyfundme import app
from itsdangerous import SignatureExpired
from flask_mail import Message
from flask_login import login_required, logout_user, current_user, login_user
from .. import mail
from partyfundme.utils import serializer, save_picture
import requests, json
import secrets
import os


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
            return redirect(url_for('main.home'))

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

@users.route("/profile")
@login_required
def profile():
    """User profile logic."""
    form = UpdateAccountForm()

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('/users/user-profile.html', 
                            image_file=image_file,  form=form)

@users.route("/account", methods=['GET','POST'])
@login_required
def edit_profile():
    """User profile logic."""
    form = UpdateAccountForm()

    if request.method == 'POST':
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.edit_profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('/users/user-edit-profile.html', 
                            image_file=image_file,  form=form)


@users.route("/profile/<int:user_id>/delete", methods=["POST"])
@login_required
def delete_profile(user_id):
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User Account Deleted.")

    return redirect("/")


