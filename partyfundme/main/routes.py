from flask import render_template, request, Blueprint
from flask_login import current_user, login_required
from ..models import Event, Bar


main = Blueprint('main', __name__, template_folder='templates', static_folder='static')


@main.route("/")
# @login_required
def home():
    bars = Bar.query.all()
    events = Event.query.all()
    
    
    user = current_user
    return render_template('main/home.html', events=events, bars=bars)


@main.route("/about")
def about():
    return render_template('about.html', title='About')