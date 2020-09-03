from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.html5 import DateField, TimeField
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from partyfundme.models import Bar

def choice_query():
    return Bar.query

class CreateEventForm(FlaskForm):
    """Create Events Form."""
    name_of_event = StringField(
        'Name of Event',
        validators=[DataRequired(), Length(max=22)]
    )
    event_flyer_img = FileField(
        'Add Flyer Image',
        validators=[FileAllowed(['png','jpg','gif'])]
    )
    desc = TextAreaField(
        'Description',
        validators=[DataRequired(),Length(max=255)]
    )
    number_of_guests = StringField(
        'Max Number of Guests',
        validators=[DataRequired()]
    )
    date_of_party = DateField(
        'Date of Party', 
        format='%Y-%m-%d'
    )
    time_of_party = TimeField(
        'Time of Party', 
        validators=[DataRequired()]
    )
    target_goal = StringField(
        'Target Goal',
        validators=[DataRequired()]
    )
    
    desc = TextAreaField(
        'Description',
        validators=[DataRequired()]
    )
    venue = QuerySelectField(
        query_factory=choice_query,
        allow_blank=True
    )


    
        
class UpdateEventForm(FlaskForm):
    """Update Event Form."""
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
        'Max Number of Guests',
        validators=[DataRequired()]
    )
    date_of_party = DateField('Date of Party', 
        format='%Y-%m-%d',
        validators=[DataRequired()]
    )
    time_of_party = TimeField(
        'Time of Party', 
        validators=[DataRequired()]
    )
    target_goal = StringField(
        'Target Goal',
        validators=[DataRequired()]
    )
   
    desc = TextAreaField(
        'Description',
        validators=[DataRequired()]
    )
    venue = QuerySelectField(
        query_factory=choice_query,
        allow_blank=True
    )
    submit = SubmitField('Update')
        



       