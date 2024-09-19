from app_alma.models import User, Coach
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationCoachTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
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
        self.coach = Coach.objects.create(
            name="test",
            specialty="test specialty",
            email="test@mail.com",
            phone="99 99999-9999",
        )

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
