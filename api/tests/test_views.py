from django.test import TestCase

# Create your tests here.
class HomeViewTestCase(TestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        print('####calling test_home_status_code')
        self.assertEqual(response.status_code,200)