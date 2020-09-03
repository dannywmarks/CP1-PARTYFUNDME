from partyfundme.models import db, Bar, User, Event
from run import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

with app.app_context():

  


# pylint: disable=E1101
#Create all tables
  db.drop_all()
  db.create_all()

  u1 = User(
    name="damage1", 
    email="damage1@me.com", 
    username="damage1", 
    password=(bcrypt.generate_password_hash("testyou")).decode('utf8')
  )
  u2 = User(
    name="damage2", 
    email="damage2@me.com", 
    username="damage2", 
    password=(bcrypt.generate_password_hash("testyou")).decode('utf8')
  )
  u3 = User(
    name="damage3", 
    email="damage3@me.com", 
    username="damage3", 
    password=(bcrypt.generate_password_hash("testyou")).decode('utf8')
  )
  u4 = User(
    name="damage4", 
    email="damage4@me.com", 
    username="damage4", 
    password=(bcrypt.generate_password_hash("testyou")).decode('utf8')
  )
  u5 = User(
    name="damage5", 
    email="damage5@me.com", 
    username="damage5", 
    password=(bcrypt.generate_password_hash("testyou")).decode('utf8')
  )
  u6 = User(
    name="damage6", 
    email="damage6@me.com", 
    username="damage6", 
    password=(bcrypt.generate_password_hash("testyou")).decode('utf8')
  )

  db.session.add(u1)
  db.session.add(u2)
  db.session.add(u3)
  db.session.add(u4)
  db.session.add(u5)
  db.session.add(u6)

  db.session.commit()


  b1 = Bar(
    bar_name="Benders", 
    address="806 S Van Ness Ave", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="benders@benders.com", 
    phone="(415) 824-1800", 
    img="../../../static/bars/profile_pics/benders1.jpg",
    img_header="../../../static/bars/profile_pics/benders2.jpg", 
    desc="We like to keep it real at Benders. Swing by for a brew and grab some grub from our new kitchen. Play a game of pinball, hang out on the patio or check out a burlesque show.",
    website="www.bendersbar.com", 
    facebook="benders_sf", 
    instagram="benders_sf", 
    twitter="benders_sf" 
  )
  b2 = Bar(
    bar_name="Zeitgest", 
    address="199 Valencia St", 
    city="san francisco", 
    state="CA", 
    country="usa", 
    email="zeitgeist@hotmail.com", 
    phone="(415)255-7505", 
    img="../../../static/bars/profile_pics/zeitgeist1.png",
    img_header="../../../static/bars/profile_pics/zeitgeist2.jpg", 
    desc="Founded in 1977, the bar and beer garden Zeitgeist is a Historic Legacy Business in San Francisco. One of the few bars with outdoor seating in chilly San Francisco, Zeitgeist remains the spirit of the times, true to its name.", 
    website="www.zeitgeistsf.com", 
    facebook="zg_sf", 
    instagram="zg_sf", 
    twitter="zg_sf" 
  )
  b3 = Bar(
    bar_name="Thee Parkside SF", 
    address="1600 17th St", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="theeparkside@theeparkside.com", 
    phone="(415) 252-1330", 
    img="../../../static/bars/profile_pics/theeparkside.jpg",
    img_header="../../../static/bars/profile_pics/theeparkside1.png",
    desc="Watering hole with a backyard & a small stage hosting bands spanning indie, punk, metal & country", 
    website="www.theeparkside.com", 
    facebook="theeparkside_sf", 
    instagram="theeparkside_sf", 
    twitter="theeparkside_sf" 
  )
  b4 = Bar(
    bar_name="Lucky 13", 
    address="2140 Market St", 
    city="San Francisco", 
    state="CA", 
    country="usa", 
    email="lucky13@me.com", 
    phone="(415) 487-1313", 
    img="../../../static/bars/profile_pics/lucky13.jpg",
    img_header="../../../static/bars/profile_pics/lucky13one.jpg",
    desc="No-frills rock 'n' roll spot with pinball, pool tables & punk rock on the jukebox. Cash only.", 
    website="www.lucky13.com", 
    facebook="lucky13", 
    instagram="lucky13", 
    twitter="lucky13" 
  )
  b5 = Bar(
    bar_name="Emporium SF",
    address="1616 Divisadero St", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="emporium@sf.com", 
    phone="(773) 697-7922", 
    img="../../../static/bars/profile_pics/emporiumsf1.jpg",
    img_header="./../../static/bars/profile_pics/emporiumsf2.jpg",
    desc="Emporium SF's most innovative entertainment destination! We have the largest collection of games in San Francisco with everything from classic arcade games to pool tables to tons of pinball, foosball, skeeball, air hockey, and more! ", 
    website="www.emporiumsf.com", 
    facebook="empsf", 
    instagram="empsf", 
    twitter="empsf" 
  )
  b6 = Bar(
    bar_name="Emperor Nortons", 
    address="510 Larkin", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="empnsf@me.com", 
    phone="(415) 926-8118", 
    img="../../../static/bars/profile_pics/empnortons1.jpg",
    img_header="../../../static/bars/profile_pics/empnortons2.png", 
    desc="Rock n Roll Lounge in the heart of the City", 
    website="www.empnsf.com", 
    facebook="empnsf", 
    instagram="empnsf", 
    twitter="empnsf" 
  )

  db.session.add(b1)
  db.session.add(b2)
  db.session.add(b3)
  db.session.add(b4)
  db.session.add(b5)
  db.session.add(b6)

  db.session.commit()


  e1 = Event(
    name_of_event="Daniel's Birthday",
    event_flyer_img="",
    desc="Daniel's Bday Party",
    number_of_guests="50",
    date_of_party="05-03-2020",
    time_of_party="9:00",
    target_goal="$1500",
    total_fund=55,
    )
  e2 = Event(
    name_of_event="Covid-19 Celebration",
    event_flyer_img="",
    desc="Celebrating not having covid-19",
    number_of_guests="20",
    date_of_party="02-13-2020",
    time_of_party="9:00",
    target_goal="$500",
    total_fund=600,
    )
  e3 = Event(
    name_of_event="MoneyShot Promo",
    event_flyer_img="",
    desc="Promo for App launch",
    number_of_guests="100",
    date_of_party="09-23-2020",
    time_of_party="9:00",
    target_goal="$2500",
    total_fund=3000,
    )
  e4 = Event(
    name_of_event="Powerhouse Productions",
    event_flyer_img="",
    desc="Live Music: Madball, Agnostic Front, Skarhead",
    number_of_guests="300",
    date_of_party="07-13-2020",
    time_of_party="9:00",
    target_goal="$2000",
    total_fund=2500
    )
  e5 = Event(
    name_of_event="Tommy's Graduation",
    event_flyer_img="",
    desc="Little Tommy graduating college",
    number_of_guests="40",
    date_of_party="05-03-2020",
    time_of_party="9:00",
    target_goal="$1000",
    total_fund=2000,
    )
  e6 = Event(
    name_of_event="Arcade Tournamet",
    event_flyer_img="",
    desc="Arcade Tournament",
    number_of_guests="200",
    date_of_party="05-03-2020",
    time_of_party="9:00",
    target_goal="$5000",
    total_fund=3300,
    )


  db.session.add(e1)
  db.session.add(e2)
  db.session.add(e3)
  db.session.add(e4)
  db.session.add(e5)
  db.session.add(e6)

  db.session.commit()
