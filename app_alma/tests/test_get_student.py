from app_alma.models import User, Student
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetStudentTestCase(APITestCase):
    fixtures = ["database_prototype.json"]

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.student = Student.objects.get(pk=4)

    def test_STUDENT_GET_request(self):
        """Get request test for Student"""
        self.url = reverse("student-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_STUDENT_GET_ID_request(self):
        """Get ID request test for Student"""
        self.url = reverse("student-id-list", kwargs={"pk": self.student.pk})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
