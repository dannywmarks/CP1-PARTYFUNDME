from partyfundme import create_app
from unittest import TestCase
from flask import current_app
from flask_login import current_user


class TestTestCase(TestCase): 
    app = create_app()
      
    app.app_context().push()
    def test_home_page(self):
      """Testing main page view """

      with current_app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<i class="fas fa-arrow-right"> Mission Statment</i>', html)

    def test_login_page(self):
      """ Testing login page view """
      with current_app.test_client() as client:
            res = client.get('/login')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h5 class="card-title text-center">Sign In</h5>', html)





    def test_register_page(self):
        """ Testing registeration page """
        with current_app.test_client() as client:
              res = client.get('/signup')
              html = res.get_data(as_text=True)

              self.assertEqual(res.status_code, 200)
              self.assertIn('<h5 class="card-title text-center">Register</h5>', html)

    
     
    def test_setup2(self):
      

      with current_app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<i class="fas fa-arrow-right"> Mission Statment</i>', html)

    def test_user_registeration(self):
      """Ensure user can register"""
      with current_app.test_client() as client:
          response = client.post('/signup', data=dict(
              name='danny ', 
              email='dannydamage@me.com', 
              username='dannydamage',
              password='damage',
              confirm='damage'
          ), follow_redirects=True)
          self.assertIn(b'User created!', response.data)
         
          # self.assertTrue(current_user.username == "tigarcia")
          # # make sure we hash the password!
          # self.assertNotEqual(current_user.password, "moxie")
          # self.assertTrue(current_user.is_authenticated)

    def test_user_registeration_user_exists(self):
      """Ensure user can register"""
      with current_app.test_client() as client:
          response = client.post('/signup', data=dict(
              name='bill', 
              email='bill@bob.com', 
              username='billybob',
              password='thorton',
              confirm='thorton'
          ), follow_redirects=True)
          self.assertIn(b'User Exists!', response.data)
          # self.assertTrue(current_user.username == "tigarcia")
          # # make sure we hash the password!
          # self.assertNotEqual(current_user.password, "moxie")
          # self.assertTrue(current_user.is_authenticated)

    def test_correct_login(self):
      """User should be authenticated upon successful login and stored in current user"""
      with current_app.test_client() as client:
          res = client.post(
              '/login',
              data=dict(email="dannydamage@me.com", password="fuckyou"),
              follow_redirects=True
          )
          
          self.assertTrue(current_user.username == "dannydamage")
          self.assertTrue(current_user.is_authenticated)

    def test_login_unconfirmed_email(self):
      """User should be authenticated upon successful login and stored in current user"""
      with current_app.test_client() as client:
          res = client.post(
              '/login',
              data=dict(email="bill@bob.com", password="thorton"),
              follow_redirects=True
          )
          
          self.assertIn(b'Must confirm email before logging in', res.data)
          


    def test_incorrect_login(self):
      """The correct flash message is sent when incorrect info is posted"""
      with current_app.test_client() as client:
        res = client.post(
         '/login',
          data=dict(email="dsadsa@me.com", password="dsadsadsa"),
          follow_redirects=True
         )
        self.assertIn(b'Invalid username/password combination', res.data)
    
    def test_logout(self):
      """ Make sure log out actually logs out a user """
      with current_app.test_client() as client:
        client.post(
          '/login',
          data=dict(email='dannydamage@me.com', password='fuckyou'),
          follow_redirects=True
        )
        res = client.get('/logout', follow_redirects=True)
        self.assertIn(b'You are logged out!', res.data)
        self.assertFalse(current_user.is_authenticated)
    
    def test_logout_route_requires_login(self):
      """Make sure that you can not log out without being logged in"""
      with current_app.test_client() as client:
        res = client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', res.data)


    