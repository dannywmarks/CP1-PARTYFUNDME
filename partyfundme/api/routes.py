from flask import Flask, request, render_template, jsonify, Blueprint
from ..models import Bar, Event

api_blueprint= Blueprint('api_blueprint', __name__)

@api_blueprint.route('/api/bars')
def get_bars():
    """ Return all bars """
    bars = [bar.to_dict() for bar in Bar.query.all()]

    return jsonify(bars=bars)

@api_blueprint.route("/api/bar/<int:bar_id>")
def get_bar(bar_id):
    """ Returns a bar """
    bar = Bar.query.get_or_404(bar_id)

    return jsonify(bar=bar.to_dict())

@api_blueprint.route('/api/events')
def get_events():
    """ Return all Events """
    events = [event.to_dict() for event in Event.query.all()]

    return jsonify(events=events)

@api_blueprint.route("/api/events/<int:event_id>")
def get_event(event_id):
    """ Returns an Event """
    event = Event.query.get_or_404(event_id)

    return jsonify(event=event.to_dict())


# @app.route('/api/cupcakes', methods=['POST'])
# def create_cupcake():
#   """Add cupcake, and return data on new cupcake"""

#   data = request.json

#   cupcake = Cupcake(
#     flavor=data['flavor'],
#     rating=data['rating'],
#     size=data['size'],
#     image=data['image'] or None
#   )

#   db.session.add(cupcake)
#   db.session.commit()

#   return (jsonify(cupcake=cupcake.to_dict()), 201)




# @app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
# def update_cupcake(cupcake_id):
#     """Update cupcake from data in request. Return updated data.

#     Returns JSON like:
#         {cupcake: [{id, flavor, rating, size, image}]}
#     """

#     data = request.json

#     cupcake = Cupcake.query.get_or_404(cupcake_id)

#     cupcake.flavor = data['flavor']
#     cupcake.rating = data['rating']
#     cupcake.size = data['size']
#     cupcake.image = data['image']

#     db.session.add(cupcake)
#     db.session.commit()

#     return jsonify(cupcake=cupcake.to_dict())

# @app.route("/api/cupcakes/<int:cupcake_id>", methods=['DELETE'])
# def remove_cupcake(cupcake_id):
#     """ Deletes a cupcake """
#     cupcake = Cupcake.query.get_or_404(cupcake_id)

#     db.session.delete(cupcake)
#     db.session.commit()

#     return jsonify(message='Deleted')