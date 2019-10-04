from django.test import TestCase
import requests

# Create your tests here.

class FunctionTest(TestCase):
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

    def test_login(self):
        result = requests.post(self.LOGIN_URL, data=self.login_data)

        self.post_body["jwt"] = result.text
        self.assertEqual(result, result)

    def test_post(self):
        result = requests.post(self.POST_URL, data=self.post_body)

        print(result)
        self.assertEqual(result, result)

