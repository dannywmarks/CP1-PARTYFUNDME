from flask import render_template, request, Blueprint, flash, redirect, url_for, Response
from .forms import CreateEventForm
from ..models import db, Event, Image
from werkzeug.utils import secure_filename
from partyfundme.users.utils import save_picture
# pylint: disable=E1101



events = Blueprint('events', __name__,template_folder='templates', static_folder='static')



@events.route("/events")
def events_list():
    events = [event.to_dict() for event in Event.query.all()]
    return render_template('events/events_list.html', events=events)

@events.route("/events/<int:event_id>")
def event(event_id):
    event = Event.query.get_or_404(event_id)
    image_file = url_for('static', filename='events/profile_pics/' + event.event_flyer_img)
    return render_template('events/events_event.html', event=event, image_file=image_file)

@events.route("/events/new_event", methods=['GET', 'POST'])
def new_event():
    form = CreateEventForm()

    if form.validate_on_submit():

        
        name_of_event = form.name_of_event.data
        event_flyer_img = form.event_flyer_img.data
        desc = form.desc.data
        number_of_guests = form.number_of_guests.data
        date_of_party = form.date_of_party.data
        target_goal = form.target_goal.data
        total_fund = form.total_fund.data
        desc = form.desc.data
        venue = form.venue.data
        
        
        print(f"{event_flyer_img}")

        event = Event.register(
            name_of_event, 
            event_flyer_img,  
            desc, 
            number_of_guests, 
            date_of_party, 
            target_goal, 
            total_fund,  
            venue,
            )
       
        db.session.add(event)
        db.session.commit()

        flash('Event created!')
        return redirect(url_for('events.events_list'))

    
    return render_template('events/events_signup.html', form=form)


