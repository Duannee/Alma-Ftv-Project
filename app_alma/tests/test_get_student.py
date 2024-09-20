from app_alma.models import User, Student
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetStudentTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
        self.student = Student.objects.create(
            name="test",
            age=21,
            email="test@mail.com",
            phone="99 99999-9999",
            category="test category",
        )

    def test_USER_GET_request(self):
        """Get request test for Student"""
        self.url = reverse("student-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
