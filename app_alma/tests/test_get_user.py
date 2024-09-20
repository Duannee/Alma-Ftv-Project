from app_alma.models import User, Coach
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")

    def test_USER_GET_request(self):
        """Get request test for User"""
        self.url = reverse("user-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_USER_GET_ID_request(self):
        """Get ID request test for User"""
        self.url = reverse("user-id-list", kwargs={"pk": self.user.pk})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
