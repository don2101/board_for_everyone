from django.test import TestCase
import requests

# Create your tests here.

class LoginTest(TestCase):
    def setUp(self):
        self.LOGIN_URL = "http://localhost:8000/accounts/signin/"
        self.login_data = {
            "username": "aaa",
            "password": "qwe",
        }

    def test_login(self):
        result = requests.post(self.LOGIN_URL, data=self.login_data)
        
        self.assertEqual(result.status_code, 200)
