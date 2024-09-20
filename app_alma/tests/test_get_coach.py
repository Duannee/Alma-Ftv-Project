from app_alma.models import User, Coach
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetCoachTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
        self.coach = Coach.objects.create(
            name="test",
            email="test@mail.com",
            phone="99 99999-9999",
            specialty="test specialty",
        )

    def test_COACH_GET_request(self):
        """Get request test for Coach"""
        self.url = reverse("coach-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
