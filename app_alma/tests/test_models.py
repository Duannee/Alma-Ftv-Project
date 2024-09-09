from django.test import TestCase
from app_alma.models import User, Student, StudentProfile, Payment, Coach


class ModelUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user test",
            email="usertest@mail.com",
        )

    def test_verify_user_attribute(self):
        """Test for verify user attributes"""
        self.assertEqual(self.user.username, "user test")
        self.assertEqual(self.user.email, "usertest@mail.com")
