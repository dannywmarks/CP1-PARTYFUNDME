"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, ValidationError
from ..models import User


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    username = StringField(
        'Username',
        validators=[
            Length(min=6),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Create Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    # submit = SubmitField('Register')

    def validate_username(self, username):
       user = User.query.filter_by(username=username.data).first()
       if user: 
           raise ValidationError('That username is taken. Please choose another')

    def validate_email(self, email):
       user = User.query.filter_by(email=email.data).first()
       if user: 
           raise ValidationError('That email is taken. Please choose another')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    # submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    username = StringField(
        'Username',
        validators=[
            Length(min=6),
            DataRequired()
        ]
    )
  

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['png','jpg','gif'])])

    submit = SubmitField('Update')
   
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user: 
                raise ValidationError('That username is taken. Please choose another')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user: 
                raise ValidationError('That email is taken. Please choose another')
