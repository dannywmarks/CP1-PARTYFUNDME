from flask import render_template, request, Blueprint


admin = Blueprint('admin', __name__)



@admin.route("/admin")
def admin_dashboard():
    
    return render_template('admin.html')


