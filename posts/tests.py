from django.test import TestCase
import requests

# Create your tests here.

class PostTest(TestCase):
    def setUp(self):
        self.LOGIN_URL = "http://localhost:8000/accounts/signin/"
        self.login_data = {
            "username": "aaa",
            "password": "qwe",
        }

        self.POST_URL = "http://localhost:8000/"
        self.post_body = {
            "title": "goodmanwfewfwe",
            "content": "contentwefewf",
        }

        result = requests.post(self.LOGIN_URL, data=self.login_data)
        
        self.post_body["token"] = result.text[1:len(result.text)-1]

    def test_post(self):
        result = requests.post(self.POST_URL, data=self.post_body)

        self.assertEqual(result.status_code, 201)

