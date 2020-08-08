from . import db, bcrypt
from flask_login import UserMixin, login_manager, current_user
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage
from .users.oauth import twitter_blueprint, google_blueprint
# pylint: disable=E1101
DEFAULT_IMAGE_URL = '' 
DEFAULT_EVENT_IMAGE_URL = ''
DEFAULT_VIDEO_URL = ''
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
    email_confirmed = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    created_on = db.Column(
       db.DateTime, 
       server_default=db.func.now()
    )
    last_login = db.Column(
        db.DateTime, 
        server_default=db.func.now(), 
        server_onupdate=db.func.now()
    )
    events = db.relationship(
        'Event', 
        backref='users', 
        lazy='dynamic'
    )

    # start register
    @classmethod
    def register(cls, name, email, username, password):
        """Register user w/hashed password and return user."""
        hashed = bcrypt.generate_password_hash(password)
        """turn byte_string into normal(unicode utf8) string"""
        hashed_utf8 = hashed.decode('utf8')

        # return instance of user w/username and hashed pwd
        return cls(name=name, email=email, username=username, password=hashed_utf8)
      # end register

    # user authetication
    @classmethod
    def authenticate(cls, email, pwd):
        """Validate that user exists and password is correct.
        Return user if valid; else return False."""

        u = User.query.filter_by(email=email).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False

    def __repr__(self):
        return '<User {}>'.format(self.username)



class OAuth(OAuthConsumerMixin, db.Model):
    """ Flask Dance OAUTH table """
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
    
twitter_blueprint.backend = SQLAlchemyStorage(OAuth, db.session, user=current_user)

google_blueprint.backend = SQLAlchemyStorage(OAuth, db.session, user=current_user)



class Bar(db.Model):
    """Bars Profile Table"""

    __tablename__ = 'bars'

    id = db.Column(
        db.Integer, 
        primary_key=True, 
        autoincrement=True
    )
    bar_name = db.Column(
        db.String(100), 
        nullable=False, 
        unique=False
    )
    address = db.Column(
        db.String(100), 
        nullable=False, 
        unique=True
    )
    city = db.Column(
        db.String(50),
        nullable=False
    )
    state = db.Column(
        db.String(50), 
        nullable=False
    )
    country = db.Column(
        db.String(25), 
        nullable=False
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    email_confirmed = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    phone = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )
    img = db.Column(
        db.String(150),
        nullable=False,
        default=DEFAULT_IMAGE_URL
    )
    desc = db.Column(
        db.String(255),
        nullable=True
    )
    website = db.Column(
        db.String(150),
        unique=True,
        nullable = True
    )
    facebook = db.Column(
        db.String(150),
        unique=True,
        nullable=True
    )
    instagram = db.Column(
        db.String(150),
        unique=True,
        nullable=True
    )
    twitter = db.Column(
        db.String(150),
        unique=True,
        nullable=True
    )
    created_on = db.Column(
        db.DateTime, 
        server_default=db.func.now()
    )
    event = db.relationship(
        'Event', 
        backref='bars', 
        lazy='dynamic'
    )

    # start register
    @classmethod
    def register(
        cls, 
        bar_name, 
        address, 
        city, 
        state, 
        country, 
        email, 
        phone, 
        img, 
        desc, 
        website, 
        facebook, 
        instagram, 
        twitter):

        # return instance of bar
        return cls(
            bar_name=bar_name,
            address=address,
            city=city,
            state=state,
            country=country,
            email=email,
            phone=phone,
            img=img,
            desc=desc,
            website=website,
            facebook=facebook,
            instagram=instagram,
            twitter=twitter)
      # end register

    def __repr__(self):
        return '<Bar {}>'.format(self.bar_name)

    def image_url(self):
        """Return default bar img."""

        return self.image or DEFAULT_IMAGE_URL
    
    def to_dict(self):
        """Serialize Bar to a dict of Bar info."""

        return {
            "id": self.id,
            "bar_name": self.bar_name,
            "info": {
                "email": self.email,
                "phone": self.phone,
                "website": self.website,
                "img": self.img,
                "desc": self.desc,
            },
            "location": {
                "address": self.address,
                "city": self.city,
                "state": self.state,
                "country": self.country,
            },
            "social_media": {
                "facebook": self.facebook,
                "instagram": self.instagram,
                "twitter": self.twitter
            }
        }

class Event(db.Model):
    """ Events Table """

    __tablename__ = 'events'


    id = db.Column(
        db.Integer, 
        primary_key=True, 
        autoincrement=True
    )
    name_of_event = db.Column(
        db.String(100), 
        nullable=False, 
        unique=False
    )
    event_flyer_img = db.Column(
        db.String(150),
        nullable=False,
        default=DEFAULT_EVENT_IMAGE_URL
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
    )
    bar_id = db.Column(
        db.Integer,
        db.ForeignKey('bars.id'),
    )
    desc = db.Column(
        db.String(255),
        nullable=False
    )
    number_of_guests = db.Column(
        db.String(50),
        nullable=False
    )
    date_of_party = db.Column(
        db.String(50),
        nullable=False
    )
    # DATECREATED TIME STAMP
    target_goal = db.Column(
        db.String(50),
        nullable=False
    )
    total_fund = db.Column(
        db.String(50),
        nullable=False
    )
    venue = db.Column(
        db.String(50),
        nullable=False
    )
    created_on = db.Column(
        db.DateTime, 
        server_default=db.func.now()
    )

    # bars = db.relationship('Bar', backref='users')

    @classmethod
    def register(
        cls, 
        name_of_event, 
        event_flyer_img,  
        desc, 
        number_of_guests, 
        date_of_party, 
        target_goal, 
        total_fund,  
        venue, 
    ):

        # return instance of bar
        return cls(
            name_of_event=name_of_event,
            event_flyer_img=event_flyer_img,
            desc=desc,
            number_of_guests=number_of_guests,
            date_of_party=date_of_party,
            target_goal=target_goal,
            total_fund=total_fund,
            venue=venue
        )
    
    def to_dict(self):
        """Serialize Event to a dict of Event info."""

        return {
            "id": self.id,
            "name_of_event": self.name_of_event,
            "info": {
                "event_flyer_img": self.event_flyer_img,
                "desc": self.desc,
                "number_of_guests": self.number_of_guests,
                "date_of_party": self.date_of_party,
                "target_goal": self.target_goal,
                "total_fund": self.total_fund
            },
            "location": {
                "venue": self.venue
            } 
        }

    def __repr__(self):
        return '<Event {}>'.format(self.name_of_event)
    
    

class EventListBars(db.Model):
    """Mapping of a event to a bar."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'eventlist_bars'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    bar_id = db.Column(db.Integer, db.ForeignKey('bars.id'))


class Image(db.Model):
    """ Model for image to event,bar,profile """

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
