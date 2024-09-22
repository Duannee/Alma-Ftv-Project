from django.test import TestCase
from app_alma.models import User, Student, StudentProfile, Payment, Coach


class FixturesTestCase(TestCase):
    fixtures = ["database_prototype.json"]

    def test_fixtures_loading(self):
        """Test to verify fixtures loading"""
        user = User.objects.get(username="duanne")
        student = Student.objects.get(pk=2)
        student_profile = StudentProfile.objects.get(pk=6)
        payment = Payment.objects.get(pk=5)
        coach = Coach.objects.get(pk=2)
        self.assertEqual(user.email, "duanne@mail.com")
        self.assertEqual(student.category, "Avancado")
        self.assertEqual(student_profile.goal, "Ser excelente")
        self.assertEqual(payment.status, "Pending")
        self.assertEqual(coach.name, "Caio")
