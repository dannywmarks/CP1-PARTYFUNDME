from flask import render_template, request, Blueprint, redirect, url_for


users = Blueprint('users', __name__)



@users.route("/login")
def login():
    
    return render_template('login.html')

@users.route("/signup")
def signup():
    
    return render_template('singup.html')

@users.route("/logout")
def logout():
    
    return redirect(url_for('main.home'))