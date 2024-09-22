from django.test import TestCase
from app_alma.models import User, Student


class FixturesTestCase(TestCase):
    fixtures = ["database_prototype.json"]

    def test_fixtures_loading(self):
        """Test to verify fixtures loading"""
        user = User.objects.get(username="duanne")
        student = Student.objects.get(pk=2)
        self.assertEqual(user.email, "duanne@mail.com")
        self.assertEqual(student.category, "Avancado")
