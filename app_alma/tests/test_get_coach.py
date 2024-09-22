from app_alma.models import User, Coach
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetCoachTestCase(APITestCase):
    fixtures = ["database_prototype.json"]

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.coach = Coach.objects.get(pk=2)

    def test_COACH_GET_request(self):
        """Get request test for Coach"""
        self.url = reverse("coach-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_COACH_GET_ID_request(self):
        """Get ID request test for Coach"""
        self.url = reverse("coach-id-list", kwargs={"pk": self.coach.pk})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
