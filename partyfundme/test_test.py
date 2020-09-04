from partyfundme import create_app
from unittest import TestCase
from flask import current_app
from .models import db, User
import os



class TestTestCase(TestCase): 

    def setUp(self):
      self.app = create_app()
      self.app_context = self.app.app_context()
      self.app_context.push()
      self.client = self.app.test_client()
      
    def tearDown(self):
      self.app_context.pop()
      


    def test_setup(self):
      
      res = self.client.get('/')
      html = res.get_data(as_text=True)

      self.assertEqual(res.status_code, 200)
      self.assertIn('<i class="fas fa-arrow-right"> Mission Statment</i>', html)

# if __name__ == '__main__':
#   unittest.main()