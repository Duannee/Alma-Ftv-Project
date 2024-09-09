from django.test import TestCase
from app_alma.models import User, Student, StudentProfile, Payment, Coach


class ModelUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user test",
            email="usertest@mail.com",
        )

    def test_verify_user_attribute(self):
        """Test for verify USER attributes"""
        self.assertEqual(self.user.username, "user test")
        self.assertEqual(self.user.email, "usertest@mail.com")


class ModelStudentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Student test",
            age="26",
            email="studentest@mail.com",
            phone="21 99999-9999",
            category="test category",
        )

    def test_verify_student_attribute(self):
        """Test for verify STUDENT attributes"""
        self.assertEqual(self.student.name, "Student test")
        self.assertEqual(self.student.age, "26")
        self.assertEqual(self.student.email, "studentest@mail.com")
        self.assertEqual(self.student.phone, "21 99999-9999")
        self.assertEqual(self.student.category, "test category")
