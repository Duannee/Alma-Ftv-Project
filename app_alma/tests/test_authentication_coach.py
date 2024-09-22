from app_alma.models import User, Coach
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationCoachTestCase(APITestCase):
    fixtures = ["database_prototype.json"]

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.client.force_authenticate(self.user)

    def test_POST_request_with_authentication(self):
        """Test to verify if Coach POST request with authentication was authorized"""
        self.url = reverse("coach-post")
        self.data = {
            "name": "test name",
            "specialty": "test specialty",
            "email": "test@mail.com",
            "phone": "99 99999-9999",
        }
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_PATCH_request_with_authentication(self):
        """Test to verify if Coach PATCH request with authentication was authorized"""

        self.coach = Coach.objects.get(pk=2)
        self.url = reverse("coach-update", kwargs={"pk": self.coach.pk})
        self.data = {
            "name": "test name",
            "specialty": "test specialty",
        }
        response = self.client.patch(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.coach.refresh_from_db()
        self.assertEqual(self.coach.name, "test name")
        self.assertEqual(self.coach.specialty, "test specialty")

    def test_DELETE_request_with_authentication(self):
        """Test to verify if Coach DELETE request with authentication was authorized"""
        self.coach = Coach.objects.get(pk=2)
        self.url = reverse("coach-delete", kwargs={"pk": self.coach.pk})
        self.assertTrue(Coach.objects.filter(pk=self.coach.pk).exists())
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Coach.DoesNotExist):
            self.coach.refresh_from_db()
