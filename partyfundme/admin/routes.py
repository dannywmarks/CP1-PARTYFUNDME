from flask import render_template, Blueprint
from .. import flaskAdmin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from ..models import User, Bar, Event, EventList, OAuth
from .. import db

admin_blueprint = Blueprint('admin_blueprint', __name__, template_folder='templates')


# Views in the ADMIN panel
flaskAdmin.add_view(ModelView(User, db.session))
flaskAdmin.add_view(ModelView(Bar, db.session))
flaskAdmin.add_view(ModelView(Event, db.session))
flaskAdmin.add_view(ModelView(EventList, db.session))
flaskAdmin.add_view(ModelView(OAuth, db.session))



@admin_blueprint.route("/admin_blueprint")
def admin_dashboard():
    return render_template('admin.html')


