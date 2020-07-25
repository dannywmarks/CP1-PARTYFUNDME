from partyfundme.models import db, Bar, User, Event
from run import app

with app.app_context():


# pylint: disable=E1101
#Create all tables
  db.drop_all()
  db.create_all()

  u1 = User(
    name="damage1", 
    email="damage1@me.com", 
    username="damage1", 
    password="testyou"
  )
  u2 = User(
    name="damage2", 
    email="damage2@me.com", 
    username="damage2", 
    password="testyou"
  )
  u3 = User(
    name="damage3", 
    email="damage3@me.com", 
    username="damage3", 
    password="testyou"
  )
  u4 = User(
    name="damage4", 
    email="damage4@me.com", 
    username="damage4", 
    password="testyou"
  )
  u5 = User(
    name="damage5", 
    email="damage5@me.com", 
    username="damage5", 
    password="testyou"
  )
  u6 = User(
    name="damage6", 
    email="damage6@me.com", 
    username="damage6", 
    password="testyou"
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
    address="123 valencie", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="benders@benders.com", 
    phone="555-5555", 
    img="", 
    desc="i'm a bar", 
    website="www.benders.com", 
    facebook="benders_sf", 
    instagram="benders_sf", 
    twitter="benders_sf" 
  )
  b2 = Bar(
    bar_name="Zeitgest", 
    address="456 valencia", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="zeitgeist@hotmail.com", 
    phone="555-5556", 
    img="", 
    desc="i'm a bar", 
    website="www.zeitgeist.com", 
    facebook="zg_sf", 
    instagram="zg_sf", 
    twitter="zg_sf" 
  )
  b3 = Bar(
    bar_name="Hemlock", 
    address="123 polk st", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="hemlock@hemlock.com", 
    phone="555-5557", 
    img="", 
    desc="i'm a bar", 
    website="www.hemlock.com", 
    facebook="hemlock_sf", 
    instagram="hemlock_sf", 
    twitter="hemlock_sf" 
  )
  b4 = Bar(
    bar_name="Lucky 13", 
    address="123 market st", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="lucky13@me.com", 
    phone="555-5558", 
    img="", 
    desc="i'm a bar", 
    website="www.lucky13.com", 
    facebook="lucky13", 
    instagram="lucky13", 
    twitter="ucky13" 
  )
  b5 = Bar(
    bar_name="Emporium", 
    address="123 bryant", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="emporium@sf.com", 
    phone="555-5559", 
    img="", 
    desc="i'm a bar", 
    website="www.empsf.com", 
    facebook="empsf", 
    instagram="empsf", 
    twitter="empsf" 
  )
  b6 = Bar(
    bar_name="Emperor Nortons", 
    address="123 larkin", 
    city="san francisco", 
    state="ca", 
    country="usa", 
    email="empnsf@me.com", 
    phone="555-5550", 
    img="", 
    desc="i'm a bar", 
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
    promo_video_link="",
    desc="Daniel's Bday Party",
    number_of_guests="50",
    date_of_party="05-03-2020",
    target_goal="$1500",
    total_fund="$55",
    venue="Emperor Nortons")
  e2 = Event(
    name_of_event="Covid-19 Celebration",
    event_flyer_img="",
    promo_video_link="",
    desc="Celebrating not having covid-19",
    number_of_guests="20",
    date_of_party="02-13-2020",
    target_goal="$500",
    total_fund="$20",
    venue="Lucky13")
  e3 = Event(
    name_of_event="MoneyShot Promo",
    event_flyer_img="",
    promo_video_link="",
    desc="Promo for App launch",
    number_of_guests="100",
    date_of_party="09-23-2020",
    target_goal="$2500",
    total_fund="$3000",
    venue="Benders")
  e4 = Event(
    name_of_event="Powerhouse Productions",
    event_flyer_img="",
    promo_video_link="",
    desc="Live Music: Madball, Agnostic Front, Skarhead",
    number_of_guests="300",
    date_of_party="07-13-2020",
    target_goal="$2000",
    total_fund="$2500",
    venue="Hemlock")
  e5 = Event(
    name_of_event="Tommy's Graduation",
    event_flyer_img="",
    promo_video_link="",
    desc="Little Tommy graduating college",
    number_of_guests="40",
    date_of_party="05-03-2020",
    target_goal="$1000",
    total_fund="$200",
    venue="Emporium")
  e6 = Event(
    name_of_event="Street Fighter 2 Championships",
    event_flyer_img="",
    promo_video_link="",
    desc="Arcade Tournament",
    number_of_guests="200",
    date_of_party="05-03-2020",
    target_goal="$5000",
    total_fund="$3300",
    venue="Emporium")


  db.session.add(e1)
  db.session.add(e2)
  db.session.add(e3)
  db.session.add(e4)
  db.session.add(e5)
  db.session.add(e6)

  db.session.commit()
