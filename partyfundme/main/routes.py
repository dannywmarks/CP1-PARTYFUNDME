from flask import render_template, request, Blueprint, url_for
from flask_login import current_user, login_required
from ..models import Event, Bar
from .forms import EmailForm


main = Blueprint('main', __name__, template_folder='templates', static_folder='static')


@main.route("/")
# @login_required
def home():
    
    form = EmailForm()
    bars = Bar.query.all()
    events = Event.query.order_by(Event.id.desc()).limit(6).all()
    
    for event in events:
        image_file = url_for('static', filename='profile_pics/' + event.event_flyer_img)
        event.event_flyer_img = image_file

    user = current_user
    
    
    return render_template('main/home.html', form=form, events=events, bars=bars, user=user,image_file=image_file)


@main.route("/about")
def about():

    form = EmailForm()
    bars = Bar.query.all()
    events = Event.query.all()
    
    for event in events:
        image_file = url_for('static', filename='profile_pics/' + event.event_flyer_img)
        event.event_flyer_img = image_file

    user = current_user
    
    
    

    return render_template('hi.html', title='About', form=form)