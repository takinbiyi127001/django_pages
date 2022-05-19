from django.test import TestCase, SimpleTestCase


# Create your tests here.

class PageTest(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertTrue(response.status_code, 200)
