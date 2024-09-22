from app_alma.models import User, Student, StudentProfile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetStudentProfileTestCase(APITestCase):
    fixtures = ["database_prototype.json"]

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.student = Student.objects.get(pk=4)
        self.student_profile = StudentProfile.objects.get(pk=4)

    def test_STUDENT_PROFILE_GET_request(self):
        """Get request test for Student Profile"""
        self.url = reverse("student-profile-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_STUDENT_PROFILE_GET_ID_request(self):
        """Get ID request test for Student Profile"""
        self.url = reverse(
            "student-profile-id-list", kwargs={"pk": self.student_profile.pk}
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
