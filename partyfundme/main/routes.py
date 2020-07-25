from flask import render_template, request, Blueprint
from flask_login import current_user, login_required


main = Blueprint('main', __name__)


@main.route("/")
@login_required
def home():
    username = current_user.username
    return render_template('home.html', username=username)


@main.route("/about")
def about():
    return render_template('about.html', title='About')