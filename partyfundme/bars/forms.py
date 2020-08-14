from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional



class BarSignupForm(FlaskForm):
    """Register and Sign-up Bars Form."""
    bar_name = StringField(
        'Bar Name',
        validators=[DataRequired()]
    )
    address = StringField(
        'Address',
        validators=[DataRequired()]
    )
    city = StringField(
        'City',
        validators=[DataRequired()]
    )
    state = StringField(
        'State',
        validators=[DataRequired()]
    )
    country = StringField(
        'Country',
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
    phone = StringField(
        'Phone',
        validators=[DataRequired()]
    )
    img = StringField(
        'Bar Image',
        validators=[DataRequired()
        ]
    )
    desc = StringField(
        'Description',
        validators=[DataRequired()]
    )
    website = StringField(
        'Website',
        validators=[DataRequired()]
    )
    facebook = StringField(
        'Facebook',
        validators=[DataRequired()]
    )
    instagram = StringField(
        'Instagram',
        validators=[DataRequired()]
    )
    twitter = StringField(
        'Twitter',
        validators=[DataRequired()]
    )