from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status

class NoyonTest(APITestCase):
    def setUp(self):
        pass
    def test_noyon(self):
        url = reverse('noyon')
        data = {
            'greetings' : "Hello, i'm Noyon"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
        
    def test_noyon2(self):
        url = reverse('noyon2')
        data = {
            'greetings' : "Hello again, i'm Noyon"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
        
    def test_noyon3(self):
        url = reverse('noyon3')
        data = {
            'greetings' : "Hi There, i'm Noyon"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
        
    def test_noyon4(self):
        url = reverse('noyon4')
        data = {
            'greetings' : "Hey, i'm Noyon, What's up?"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)