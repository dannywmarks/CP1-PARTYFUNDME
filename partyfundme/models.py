from . import db, bcrypt
from flask_login import UserMixin, login_manager


# pylint: disable=E1101



class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    username = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
    )
    created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )
    last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    # start register
    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password and return user."""
        hashed = bcrypt.generate_password_hash(pwd)
        """turn byte_string into normal(unicode utf8) string"""
        hashed_utf8 = hashed.decode('utf8')

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8)
      # end register

    # user authetication
    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists and password is correct.
        Return user if valid; else return False."""

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False

    def __repr__(self):
        return '<User {}>'.format(self.username)
    

# class Bar(db.Model):
#     """Bars Table"""

#     __tablename__ = 'bars'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     bar_name = db.Column(db.String(25), nullable=False)
#     address = db.Column(db.String(50), nullable=False)
#     city = db.Column(db.String(50), nullable=False)
#     state = db.Column(db.String(2), nullable=False)
#     country = db.Column(db.String(25), nullable=False)
#     email = db.Column(db.String(100))
#     phone = db.Column(db.String(50))
#     img = db.Column(db.String(150))
#     website = db.Column(db.String(150))
#     ##### SEPERATE TABLE? #####
#     facebook = db.Column(db.String(150))
#     instagram = db.Column(db.String(150))
#     twitter = db.Column(db.String(150))
#     # DATECREATED TIMESTAMP


# class Event(db.Model):
#     """ Events Table """

#     __tablename__ = 'events'

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     bar_id = db.Column(db.Integer)
#     user_id = db.Column(db.Integer)
#     date_of_party = db.Column(db.String(25))
#     # DATECREATED TIME STAMP
#     funding_duration = db.Column(db.String(25))
#     goal = db.Column(db.String(25))
#     total_fund = db.Column(db.String(25))
#     title = db.Column(db.String(25))
#     description = db.Column(db.String(255))
#     event_flyer_img = db.Column(db.String(150))
#     promo_video = db.Column(db.String(150))
#     location = db.Column(db.String(50))
#     #### PAYMENT PROCESSORS???? ######
#     stripe = db.Column(db.String(25))
#     paypal = db.Column(db.String(25))

