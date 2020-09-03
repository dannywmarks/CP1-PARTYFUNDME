#Flask Extensions

from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin


assets = Environment()
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()
flask_mail = Mail()
flaskAdmin = Admin(template_mode='bootstrap3')



#Flask asset bundles
js = Bundle('js/stripe.js',output='main.js')

css = Bundle('style.css','events.css','bars.css', output='main.css')