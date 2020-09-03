from flask import Flask, request, render_template, jsonify, Blueprint, url_for, abort, redirect
from os import environ
import stripe

payments_blueprint= Blueprint('payments_blueprint', 
                              __name__, 
                              template_folder='templates', 
                              static_folder='static')

                             

@payments_blueprint.route('/stripe')
def stripe_payment():
  stripe.api_key = environ.get('STRIPE_SECRET_KEY')
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price': 'price_1HBNmXG5IA6daKhNqx7T7oOh',
      'quantity': 1,
    }],
    mode='payment',
    success_url=url_for('mail_blueprint.ticket', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
    cancel_url =url_for('main.home', _external=True)
  )
  return {
    'checkout_session_id' : session['id'],
    'checkout_public_key' : environ.get('STRIPE_PUBLIC_KEY')
          }

@payments_blueprint.route('/thanks')
def thanks():
    """ Stripe confirmation page """
    return render_template('payments/ticket.html')

@payments_blueprint.route('/stripe_webhook', methods=['POST'])
def stripe_webhook():
    print('WEBHOOK CALLED')

    # Making sure payload sent isn't too big
    if request.content_length > 1024 * 1024:
      print('REQUEST TO BIG')
      abort(400)
    payload = request.get_data()
    sig_header = request.environ.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = 'whsec_KpL7mkA8ozzysUCgdLCUImeWGBaTHkci'
    event = None
    
    try:
      event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
    )
    except ValueError as e:
      # Invalid Payload
      print('INVALID PAYLOAD')
      return {}, 400
    except stripe.error.SignatureVerificationError as e:
      # Invalid signature
      print('INVALID PAYLOAD')
      return {}, 400

     #Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items['data'][0]['description'])

  
  
    return {}