from flask import render_template, request, Blueprint


bars = Blueprint('bars', __name__)



@bars.route("/bars")
def bars_list():
    
    return render_template('bars_list.html')