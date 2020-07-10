from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "user.login"
    from .models import User

    # flask-login user loader
    @login_manager.user_loader
    def load_user(user_id):
      """Check if user is logged-in on every page load."""
      if user_id is not None:
        return User.query.get(user_id)
      return None


    # Register Blueprint Routes
    from partyfundme.admin.routes import admin
    from partyfundme.bars.routes import bars
    from partyfundme.events.routes import events
    from partyfundme.users.routes import users
    from partyfundme.main.routes import main

    app.register_blueprint(admin)
    app.register_blueprint(bars)
    app.register_blueprint(events)
    app.register_blueprint(users)
    app.register_blueprint(main)

    with app.app_context():
    # Create Database Models
        db.create_all()

    return app
