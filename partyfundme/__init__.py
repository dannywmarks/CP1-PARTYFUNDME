from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.google import make_google_blueprint, google
from os import environ


app = Flask(__name__, static_folder='static', template_folder='templates')
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()
mail = Mail()
flaskAdmin = Admin(template_mode='bootstrap3')


def create_app():
  

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins

    #SQLALCHEMY
    db.init_app(app)
    #BCRYPT 
    bcrypt.init_app(app)
     #FLASK LOGIN 
    login_manager.init_app(app)
    #CRSFTOKEN FOR WTFORMS
    csrf.init_app(app) 
    #FLASK MAIL
    mail.init_app(app) 
    #FLASK ADMIN
    flaskAdmin.init_app(app)
    #OAUTH 2.0
    # oauth.init_app(app) 

    login_manager.login_view = "users.login"
    

    from .models import User

    # flask-login user loader
    @login_manager.user_loader
    def load_user(user_id):
      """Check if user is logged-in on every page load."""
      if user_id is not None:
        return User.query.get(user_id)
      return None
    


    # Register Blueprint Routes
    from partyfundme.admin.routes import admin_blueprint
    from partyfundme.api.routes import api_blueprint
    from partyfundme.bars.routes import bars
    from partyfundme.events.routes import events
    from partyfundme.users.routes import users
    from partyfundme.main.routes import main
    from partyfundme.payments.routes import payments_blueprint
    from .users.oauth import oauth_blueprint
    from .mail.routes import mail_blueprint

    twitter_blueprint = make_twitter_blueprint(api_key=environ.get('TWITTER_API_KEY'), api_secret=environ.get('TWITTER_SECRET'))
    google_blueprint = make_google_blueprint(client_id=environ.get('GOOGLE_CLIENT_ID'), client_secret=environ.get('GOOGLE_SECRET'))

    app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')
    app.register_blueprint(google_blueprint, url_prefix='/google_login')

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(bars)
    app.register_blueprint(events)
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(oauth_blueprint)
    app.register_blueprint(payments_blueprint)
    app.register_blueprint(mail_blueprint)
    

    return app
