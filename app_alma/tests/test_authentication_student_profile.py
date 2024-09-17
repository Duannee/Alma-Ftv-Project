from app_alma.models import Student, StudentProfile, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationStudentProfileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
        self.student = Student.objects.create(
            name="test",
            age=21,
            email="test@mail.com",
            phone="99 99999-9999",
            category="test",
        )
        self.client.force_authenticate(self.user)

    def test_POST_request_with_authentication(self):
        """Test to verify if Student Profile POST request with authentication was authorized"""
        self.url = reverse(
            "student-profile-post", kwargs={"student_id": self.student.pk}
        )
        self.data = {
            "student": self.student.id,
            "goal": "new test goal",
            "progress": "new test progress",
            "feedback": "new test feedback",
        }
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        student_profile = StudentProfile.objects.get(student=self.student)
        self.assertEqual(student_profile.goal, "new test goal")
        self.assertEqual(student_profile.progress, "new test progress")
        self.assertEqual(student_profile.feedback, "new test feedback")

    # def test_PATCH_request_with_authentication(self):
    #     """Test to verify if Student Profile PATCH request with authentication was authorized"""
    #     self.student_profile = StudentProfile.objects.create(
    #         student=self.student,
    #         goal="test goal",
    #         progress="test progress",
    #         feedback="test feedback",
    #     )
    #     self.url = reverse(
    #         "student-profile-patch", kwargs={"pk": self.student_profile.pk}
    #     )
    #     self.data = {
    #         "goal": "new test goal",
    #         "progress": "new test progress",
    #         "feedback": "new test feedback",
    #     }
    #     response = self.client.patch(self.url, self.data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.student_profile.refresh_from_db()
    #     self.assertEqual(self.student_profile.goal, "new test goal")
    #     self.assertEqual(self.student_profile.progress, "new test progress")
    #     self.assertEqual(self.student_profile.feedback, "new test feedback")
