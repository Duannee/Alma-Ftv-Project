from app_alma.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")

    def test_USER_authentication_with_correct_credentials(self):
        """Test to verify if User credentials are correct"""
        user = authenticate(username="admin", password="admin")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_USER_authentication_with_incorrect_username(self):
        """Test to verify the authentication a incorrect username"""
        user = authenticate(username="adm", password="admin")
        self.assertFalse((user is not None) and user.is_authenticated)
