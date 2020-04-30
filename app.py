from flask import Flask, request, render_template, redirect, flash, url_for, session, logging
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from data import Events
from flask_bcrypt import Bcrypt
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from wtforms.validators import InputRequired
from forms import LoginForm

# pylint: disable=E1101

app = Flask(__name__)

Events = Events()
bcrypt = Bcrypt()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///partyfund_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def root():
    """ Root Homepage """

    return render_template("home.html")


@app.route('/how-it-works')
def about():
    """ About Homepage """

    return render_template("how-it-works.html")


@app.route('/events')
def events():
    """ Events Page """
    if "user_id" not in session:
        flash("Please login first!")
        return redirect(url_for('user_login'))
    return render_template("events.html", events=Events)


@app.route('/event/<string:id>/')
def event(id):
    """ Event Page """

    return render_template("event.html", id=id)

#######REGISTER ROUTE AND FORM MODEL###############################


class RegisterForm(Form):
    first_name = StringField('Name', [validators.Length(min=1, max=25)])
    last_name = StringField('Name', [validators.Length(min=1, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')


# class LoginForm(Form):
#     username = StringField('Username', validators=[InputRequired])
#     password = PasswordField('Password', validators=[InputRequired])


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """ Registers a user """
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        
        # errorhandlingform?
        password = bcrypt.generate_password_hash(
            form.password.data).decode('utf8')

        new_user = User(first_name=first_name, last_name=last_name,
                        email=email, username=username, password=password)

        # commit to DB
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id

        flash('You are now registered and can sign in', 'success')

        return redirect(url_for('user_login'))
    return render_template('register.html', form=form)

######## USER LOGIN ##########


@app.route('/signin', methods=['GET', 'POST'])
def user_login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f'Welcome Back, {user.first_name}!', 'success')
            session['user_id'] = user.id
            return redirect('/events')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template('signin.html', form=form)

# make a post route
@app.route('/logout')
def logout():
    """Logs user out and redirects to homepage."""

    session.pop('user_id')
    flash("Goodbye!", "success")
    return redirect("/")
