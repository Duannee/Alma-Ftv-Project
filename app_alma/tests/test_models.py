from django.test import TestCase
from app_alma.models import User, Student, StudentProfile, Payment, Coach


class ModelUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user test",
            email="usertest@mail.com",
        )

    def test_verify_user_attributes(self):
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

    def test_verify_student_attributes(self):
        """Test for verify STUDENT attributes"""
        self.assertEqual(self.student.name, "Student test")
        self.assertEqual(self.student.age, "26")
        self.assertEqual(self.student.email, "studentest@mail.com")
        self.assertEqual(self.student.phone, "21 99999-9999")
        self.assertEqual(self.student.category, "test category")


class ModelStudentProfileTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Student test",
            age="26",
            email="studentest@mail.com",
            phone="21 99999-9999",
            category="test category",
        )
        self.student_profile = StudentProfile.objects.create(
            student=self.student,
            goal="test goal",
            progress="test progress",
            feedback="test feedback",
        )

    def test_verify_student_profile_attributes(self):
        """Test for verify STUDENT PROFILE attributes"""
        self.assertEqual(self.student_profile.student, self.student)
        self.assertEqual(self.student_profile.goal, "test goal")
        self.assertEqual(self.student_profile.progress, "test progress")
        self.assertEqual(self.student_profile.feedback, "test feedback")

    def test_profile_delete_when_student_delete(self):
        """Test for verify if student profile will be delete when student will be delete"""
        self.student.delete()
        self.assertFalse(StudentProfile.objects.filter(pk=self.student.id).exists())


class ModelPaymentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Student test",
            age="26",
            email="studentest@mail.com",
            phone="21 99999-9999",
            category="test category",
        )
        self.payment = Payment.objects.create(
            student=self.student,
            pay_day="2024-09-09",
            value="290.00",
            status="test status",
        )

    def test_verify_payment_attributes(self):
        """Test for verify PAYMENT attributes"""
        self.assertEqual(self.payment.student, self.student)
        self.assertEqual(self.payment.pay_day, "2024-09-09")
        self.assertEqual(self.payment.value, "290.00")
        self.assertEqual(self.payment.status, "test status")

    def test_payment_delete_when_student_delete(self):
        """Test for verify if payment will be delete when student will be delete"""
        self.student.delete()
        self.assertFalse(Payment.objects.filter(pk=self.student.id).exists())
