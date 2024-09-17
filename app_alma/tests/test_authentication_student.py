from app_alma.models import User, Student
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationStudentTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
        self.client.force_authenticate(self.user)

    def test_POST_request_with_authentication(self):
        """Test to verify if Student POST request with authentication was authorized"""
        self.url = reverse("student-post")
        self.data = {
            "name": "test name",
            "age": 21,
            "email": "test@mail.com",
            "phone": "99 99999-9999",
            "category": "test category",
        }
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_PATCH_request_with_authentication(self):
        """Test to verify if Student PATCH request with authentication was authorized"""
        self.student = Student.objects.create(
            name="test",
            age=21,
            email="test@mail.com",
            phone="99 99999-9999",
            category="test",
        )

        self.url = reverse("student-update", kwargs={"pk": self.student.pk})
        self.data = {
            "name": "update_name",
            "category": "update_category",
        }
        response = self.client.patch(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, "update_name")
        self.assertEqual(self.student.category, "update_category")

    def test_DELETE_request_with_authentication(self):
        """Test to verify if Student DELETE request with authentication was authorized"""
        self.student = Student.objects.create(
            name="test",
            age=21,
            email="test@mail.com",
            phone="99 99999-9999",
            category="test",
        )
        self.url = reverse("student-delete", kwargs={"pk": self.student.pk})
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Student.DoesNotExist):
            self.student.refresh_from_db()
