from flask import render_template, request, Blueprint, url_for
from flask_login import current_user, login_required
from ..models import Event, Bar
import random



main = Blueprint('main', __name__, template_folder='templates', static_folder='static')


@main.route("/")
# @login_required
def home():
    
    max_model_id = Event.query.order_by(Event.id.desc())[0].id
    random_id = random.randrange(0,max_model_id)
    event = Event.query.get(random_id)
    bars = Bar.query.all()
    events = Event.query.order_by(Event.id.desc()).limit(6).all()
    
    for event in events:
        image_file = url_for('static', filename='profile_pics/' + event.event_flyer_img)
        event.event_flyer_img = image_file

    user = current_user
    
    
    return render_template('main/home.html',  events=events, bars=bars, user=user,image_file=image_file, event=event)


@main.route("/about")
def about():
    return render_template('hi.html', title='About')