from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

 

class CreateEventForm(FlaskForm):
    """Register and Sign-up Bars Form."""
    name_of_event = StringField(
        'Name of Event',
        validators=[DataRequired()]
    )
    event_flyer_img = FileField(
        'Add Flyer Image',
        validators=[FileAllowed(['png','jpg','gif'])]
    )
    desc = StringField(
        'Description',
        validators=[DataRequired()]
    )
    number_of_guests = StringField(
        'Number of Guests',
        validators=[DataRequired()]
    )
    date_of_party = StringField(
        'Date of Party',
        validators=[DataRequired()]
    )
    target_goal = StringField(
        'Target Goal',
        validators=[DataRequired()]
    )
    total_fund = StringField(
        'Total Fund',
        validators=[DataRequired()
        ]
    )
    desc = StringField(
        'Description',
        validators=[DataRequired()]
    )
    venue = StringField(
        'Venue',
        validators=[DataRequired()]
    )
    
        
        
        
        
        



       