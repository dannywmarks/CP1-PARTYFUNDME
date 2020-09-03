from flask import Flask, request, render_template, jsonify, Blueprint
from ..models import Bar, Event

api_blueprint= Blueprint('api_blueprint', __name__)

@api_blueprint.route('/api/bars')
def get_bars():
    """ Return all bars as json"""
    bars = [bar.to_dict() for bar in Bar.query.all()]

    return jsonify(bars=bars)

@api_blueprint.route("/api/bar/<int:bar_id>")
def get_bar(bar_id):
    """ Returns a bar as json """
    bar = Bar.query.get_or_404(bar_id)

    return jsonify(bar=bar.to_dict())

@api_blueprint.route('/api/events')
def get_events():
    """ Return all Events as json """
    events = [event.to_dict() for event in Event.query.all()]

    return jsonify(events=events)

@api_blueprint.route("/api/events/<int:event_id>")
def get_event(event_id):
    """ Returns an Event as json """
    event = Event.query.get_or_404(event_id)

    return jsonify(event=event.to_dict())


