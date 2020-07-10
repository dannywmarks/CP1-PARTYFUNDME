from flask import render_template, request, Blueprint


events = Blueprint('events', __name__)



@events.route("/events")
def events_list():
    
    return render_template('events_list.html')