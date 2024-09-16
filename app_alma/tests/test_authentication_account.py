from app_alma.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app_alma.serializers import UserSerializer


class AuthenticationStudentTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
        self.url = reverse("student-post")
        self.client.force_authenticate(self.user)

    def test_POST_request_with_authentication(self):
        """Test to verify if Student POST request with authentication was authorized"""
        self.data = {
            "name": "test",
            "age": 21,
            "email": "test@mail.com",
            "phone": "99 99999-9999",
            "category": "test",
        }
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
