from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status

   
class SignUpEnpointTest(APITestCase):
    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        # self.password = "you_know_nothing"
        # self.user = User.objects.create_user(self.username, self.email, self.password)
        # self.token = Token.objects.create(user=self.user)
        # self.api_authentication()
    def test_create_account(self):
        """
        Ensure we can create a new account object.
		email = serializers.CharField(required=True)
		password = serializers.CharField(required=True)
		phone_no = serializers.CharField(required=True)
		address = serializers.CharField(required=True)
		sex = serializers.CharField(required=True)
		profession = serializers.CharField(required=True)
		date_of_birth = serializers.CharField(required=True)
        """
        url = reverse('signup')
        data = {
			'email': 'DabApps',	
			'password': 'DabApps'
		}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(response.data, data)