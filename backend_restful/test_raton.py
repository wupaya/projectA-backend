from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status

class RatonTest(APITestCase):
    def setUp(self):
        pass
    def test_raton(self):
        url = reverse('raton')
        data = {
            'greetings' : "Hello, i'm Raton"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)