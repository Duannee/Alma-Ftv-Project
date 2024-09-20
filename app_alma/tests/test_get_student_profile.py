from app_alma.models import User, Student, StudentProfile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetStudentProfileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
        self.student = Student.objects.create(
            name="test",
            age=21,
            email="test@mail.com",
            phone="99 99999-9999",
            category="test category",
        )
        self.student_profile = StudentProfile.objects.create(
            student=self.student,
            goal="test goal",
            progress="test progress",
            feedback="test feedback",
        )

    def test_USER_GET_request(self):
        """Get request test for Student Profile"""
        self.url = reverse("student-profile-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_USER_GET_ID_request(self):
        """Get ID request test for Student Profile"""
        self.url = reverse(
            "student-profile-id-list", kwargs={"pk": self.student_profile.pk}
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
