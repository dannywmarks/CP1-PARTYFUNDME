from flask import render_template, request, Blueprint, flash, redirect, url_for, Response
from .forms import CreateEventForm, UpdateEventForm
from ..models import db, Event
from flask_login import current_user
from werkzeug.utils import secure_filename
from partyfundme.utils import save_picture
# pylint: disable=E1101



events = Blueprint('events', __name__,template_folder='templates', static_folder='static')



@events.route("/events")
def events_list():
    events = [event.to_dict() for event in Event.query.all()]
    return render_template('events/events_list.html', events=events)

@events.route("/my_events")
def my_events():
    user = current_user
    return render_template('events/events_my_events.html', user=user)



@events.route("/events/<int:event_id>")
def event(event_id):
    event = Event.query.get_or_404(event_id)
    event.event_flyer_img = url_for('static', filename='profile_pics/' + event.event_flyer_img)
    event_poster = event.event_flyer_img
    return render_template('events/events_event.html', event=event, event_poster=event_poster )

@events.route("/events/<int:event_id>/update", methods=['GET', 'POST'])
def update_event(event_id):

    form = UpdateEventForm()
    event = Event.query.get_or_404(event_id)

    if request.method == 'POST':
        if form.event_flyer_img.data:
           picture_file = save_picture(form.event_flyer_img.data)
           event.event_flyer_img = picture_file
        event.name_of_event = form.name_of_event.data
        event.number_of_guests = form.number_of_guests.data
        event.date_of_party = form.date_of_party.data
        event.time_of_party = form.time_of_party.data
        event.target_goal = form.target_goal.data
        event.total_fund = form.total_fund.data
        event.desc = form.desc.data
        db.session.commit()
        flash('Your Event has been updated!', 'success')
        return redirect(url_for('events.update_event', event_id=event.id))

    elif request.method == 'GET':
        
        form.name_of_event.data = event.name_of_event
        form.number_of_guests.data = event.number_of_guests
        form.date_of_party.data = event.date_of_party
        form.time_of_party.data = event.time_of_party
        form.target_goal.data = event.target_goal
        form.total_fund.data = event.total_fund
        form.desc.data = event.desc
        

    image_file = url_for('static', filename='profile_pics/' + event.event_flyer_img)
    return render_template('events/events_update_event.html', event=event, image_file=image_file, form=form)


@events.route("/events/new_event", methods=['GET', 'POST'])
def new_event():
    form = CreateEventForm()

    if request.method == 'POST':
    
        picture_file = save_picture(form.event_flyer_img.data)
           
        event_flyer_img = picture_file
        name_of_event = form.name_of_event.data
        desc = form.desc.data
        number_of_guests = form.number_of_guests.data
        date_of_party = form.date_of_party.data
        time_of_party = form.date_of_party.data
        target_goal = form.target_goal.data
        total_fund = form.total_fund.data
        desc = form.desc.data
        venue = form.venue.data
       

        event = Event.register(
            name_of_event, 
            event_flyer_img,  
            desc, 
            number_of_guests, 
            date_of_party, 
            time_of_party,
            target_goal, 
            total_fund,  
            )

        event.bars.append(venue)
       
        db.session.add(event)
        db.session.commit()

        flash('Event created!')
        return redirect(url_for('events.events_list'))

    
    return render_template('events/events_signup.html', form=form)




    
                        
