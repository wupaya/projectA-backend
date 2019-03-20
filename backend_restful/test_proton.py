from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status

class ProtonTest(APITestCase):
    def setUp(self):
        pass
    def test_proton(self):
        url = reverse('proton')
        data = {
            'greetings' : "Hello, i'm Proton"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
        
    def test_proton2(self):
        url = reverse('proton2')
        data = {
            'greetings' : "Hello again, i'm Proton"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
        
    def test_proton3(self):
        url = reverse('proton3')
        data = {
            'greetings' : "Hi There, i'm Proton"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
        
    def test_proton4(self):
        url = reverse('proton4')
        data = {
            'greetings' : "Hey, i'm Proton, What's up?"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
        
    def test_proton5(self):
        url = reverse('proton5')
        data = {
            'greetings' : "Hey, i'm Proton, How can i help you?"
            
        }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)