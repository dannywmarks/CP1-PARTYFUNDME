from flask import render_template, request, Blueprint, session,url_for, redirect
from .. import flaskAdmin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from ..models import User, Bar, Event, EventList, OAuth
from flask_login import current_user
from .. import db

admin_blueprint = Blueprint('admin_blueprint', __name__, template_folder='templates')


# Views in the ADMIN panel
flaskAdmin.add_view(ModelView(User, db.session))
flaskAdmin.add_view(ModelView(Bar, db.session))
flaskAdmin.add_view(ModelView(Event, db.session))
flaskAdmin.add_view(ModelView(EventList, db.session))
flaskAdmin.add_view(ModelView(OAuth, db.session))



class AdminView(ModelView):

    def is_accessible(self):
        return session.get('user') == 'Administrator'

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.home', next=request.url))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.home', next=request.url))

@admin_blueprint.route("/admin_blueprint")
def admin_dashboard():
    return render_template('admin.html')


