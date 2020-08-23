# pylint: disable=E1101
from flask import render_template, request, Blueprint, flash, redirect, url_for
from ..models import db, Bar
from .forms import BarSignupForm


bars = Blueprint('bars', __name__, template_folder='templates', static_folder='static')

@bars.route("/bars/signup", methods=['GET', 'POST'])
def signup():
    form = BarSignupForm()

    if form.validate_on_submit():

        bar_name = form.bar_name.data
        address = form.address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        email = form.email.data
        phone = form.phone.data
        img = form.img.data
        img_header = form.img.data
        desc = form.desc.data
        website = form.website.data
        facebook = form.facebook.data
        instagram = form.instagram.data
        twitter = form.twitter.data

        bar = Bar.register(bar_name,address,city,state,country,email,phone,img,img_header,desc,website,facebook,instagram,twitter)
       
        db.session.add(bar)
        db.session.commit()

        flash('Bar created!')
        return redirect(url_for('bars.bars_list'))

    return render_template('bars/bars_signup.html', form=form)

@bars.route("/bars")
def bars_list():

    page = request.args.get('page',1, type=int)
    bars = Bar.query.paginate(page=page, per_page=3)

    return render_template('bars/bars_list.html', bars=bars)

@bars.route("/bars/<int:bar_id>")
def bars_profile(bar_id):

    bar = Bar.query.get_or_404(bar_id)
   

    return render_template('bars/bars_profile.html', bar=bar)