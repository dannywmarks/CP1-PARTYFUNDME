from flask import render_template, request, Blueprint
from .. import flaskAdmin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from ..models import User, Bar
from .. import db

admin_blueprint = Blueprint('admin_blueprint', __name__)

flaskAdmin.add_view(ModelView(User, db.session))
flaskAdmin.add_view(ModelView(Bar, db.session))



@admin_blueprint.route("/admin_blueprint")
def admin_dashboard():
    
    return render_template('admin.html')


