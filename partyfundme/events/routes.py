from flask import render_template, request, Blueprint, flash, redirect, url_for
from .forms import CreateEventForm
from ..models import db, Event
# pylint: disable=E1101
events = Blueprint('events', __name__)



@events.route("/events")
def events_list():
    events = [event.to_dict() for event in Event.query.all()]
    return render_template('events_list.html', events=events)

@events.route("/events/signup", methods=['GET', 'POST'])
def signup():
    form = CreateEventForm()

    if form.validate_on_submit():

        
        name_of_event = form.name_of_event.data
        event_flyer_img = form.event_flyer_img.data
        promo_video_link = form.promo_video_link.data
        desc = form.desc.data
        number_of_guests = form.number_of_guests.data
        date_of_party = form.date_of_party.data
        target_goal = form.target_goal.data
        total_fund = form.total_fund.data
        desc = form.desc.data
        venue = form.venue.data
        

        event = Event.register(
            name_of_event, 
            event_flyer_img, 
            promo_video_link, 
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

    
    return render_template('events_signup.html', form=form)