from flask import render_template, Blueprint, redirect, url_for, flash, abort, session
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized
from os import environ, path
from sqlalchemy.orm.exc import NoResultFound
from flask_login import login_user




oauth_blueprint = Blueprint('oauth_blueprint', __name__)

twitter_blueprint = make_twitter_blueprint(api_key=environ.get('TWITTER_API_KEY'), api_secret=environ.get('TWITTER_SECRET'))
google_blueprint = make_google_blueprint(client_id=environ.get('GOOGLE_CLIENT_ID'), client_secret=environ.get('GOOGLE_SECRET'))


@oauth_blueprint.route('/twitter')
def twitter_login():
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    account_info = twitter.get('account/settings.json')
    account_info_json = account_info.json()
    print(f'{account_info_json}')
    return '<h1>Your Twitter name is @{}</h1>'.format(account_info_json['screen_name'])
    

@oauth_authorized.connect_via(twitter_blueprint)
def twitter_logged_in(blueprint, token):
    from ..models import User, db
    account_info = blueprint.session.get('account/settings.json')
    
    if account_info.ok:
        account_info_json = account_info.json()
        username = account_info_json['screen_name']

        query = User.query.filter_by(username=username)

        try: 
            user = query.one()
        except NoResultFound:
            user = User(username=username)
            # pylint: disable=E1101
            db.session.add(user)
            db.session.commit()

        login_user(user)
        
        

@oauth_blueprint.route('/google')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    account_info = google.get('userinfo.json')

    if account_info.ok:
        account_info_json = account_info.json()
        return '<h1>Your google email is @{}</h1>'.format(account_info_json['user_info'])
    return '<h1>You Request Failed</h1>'

# @oauth_blueprint.route("/login")
# def login():
#     """ Login user. Authorize routes."""
#     google = oauth.create_client('google')
#     redirect_uri = url_for('users.authorize', _external=True)
#     return google.authorize_redirect(redirect_uri)


# @oauth_blueprint.route("/authorize")
# def authorize():
#     google = oauth.create_client('google')  # create the google oauth client
#     token = google.authorize_access_token()  # Access token from google (needed to get user info)
#     resp = google.get('userinfo', token=token)  # userinfo contains stuff u specificed in the scrope
#     user_info = resp.json()
#     user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
#     # Here you use the profile/user data that you got and query your database find/register the user
#     # and set ur own data in the session not the profile from google
#     # session['profile'] = user_info
#     # session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
#     return redirect(url_for('bars.signup'))