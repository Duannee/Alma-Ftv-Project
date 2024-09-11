from django.test import TestCase
from app_alma.models import User, Student, StudentProfile, Payment, Coach
from app_alma.serializers import (
    UserSerializer,
    StudentSerializer,
    StudentProfileSerializer,
    PaymentSerializer,
    CoachSerializer,
)


class SerializerUserTestCase(TestCase):
    def setUp(self):
        self.user = User(
            username="user test",
            email="usertest@mail.com",
        )
        self.user_serializer = UserSerializer(instance=self.user)

    def test_verify_User_fields_serialized(self):
        """Test to verify if User fields are serialized"""
        data = self.user_serializer.data
        self.assertEqual(set(data.keys()), set(["id", "username", "email"]))

    def test_verify_content_User_fields_serializer(self):
        """Test to verify the content into the fields User serializer"""
        data = self.user_serializer.data
        self.assertEqual(data["username"], self.user.username)
        self.assertEqual(data["email"], self.user.email)


class SerializerStudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name="Student test",
            age=26,
            email="studentest@mail.com",
            phone="21 99999-9999",
            category="test category",
        )
        self.student_serializer = StudentSerializer(instance=self.student)

    def test_verify_Student_fields_serialized(self):
        """Test to verify if Student fields are serialized"""
        data = self.student_serializer.data
        self.assertEqual(
            set(data.keys()), set(["id", "name", "age", "email", "phone", "category"])
        )

    def test_verify_content_Student_fields_serializer(self):
        """Test to verify the content into the fields Student serializer"""
        data = self.student_serializer.data
        self.assertEqual(data["name"], self.student.name)
        self.assertEqual(data["age"], self.student.age)
        self.assertEqual(data["email"], self.student.email)
        self.assertEqual(data["phone"], self.student.phone)
        self.assertEqual(data["category"], self.student.category)


class SerializerStudentProfileTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name="Student test",
            age=26,
            email="studentest@mail.com",
            phone="21 99999-9999",
            category="test category",
        )
        self.student_profile = StudentProfile(
            student=self.student,
            goal="test goal",
            progress="test progress",
            feedback="test feedback",
        )
        self.student_profile_serializer = StudentProfileSerializer(
            instance=self.student_profile
        )

    def test_verify_Student_Profile_fields_serialized(self):
        """Test to verify if Student Profile fields are serialized"""
        data = self.student_profile_serializer.data
        self.assertEqual(
            set(data.keys()), set(["id", "student", "goal", "progress", "feedback"])
        )

    def test_verify_content_Student_Profile_fields_serializer(self):
        """Test to verify the content into the fields Student Profile serializer"""
        data = self.student_profile_serializer.data
        serialized_student = StudentSerializer(self.student_profile.student).data

        self.assertEqual(data["student"], serialized_student)
        self.assertEqual(data["goal"], self.student_profile.goal)
        self.assertEqual(data["progress"], self.student_profile.progress)
        self.assertEqual(data["feedback"], self.student_profile.feedback)


class SerializerPaymentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name="Student test",
            age="26",
            email="studentest@mail.com",
            phone="21 99999-9999",
            category="test category",
        )
        self.payment = Payment(
            student=self.student,
            pay_day="2024-09-09",
            value="290.00",
            status="test status",
        )
        self.payment_serializer = PaymentSerializer(instance=self.payment)

    def test_verify_Payment_fields_serialized(self):
        """Test to verify if Payment fields are serialized"""
        data = self.payment_serializer.data
        self.assertEqual(
            set(data.keys()), set(["id", "student", "pay_day", "value", "status"])
        )

    def test_verify_content_Payment_fields_serializer(self):
        """Test to verify the content into the fields Payment serializer"""
        data = self.payment_serializer.data
        serialized_student = StudentSerializer(self.payment.student).data
        self.assertEqual(data["student"], serialized_student)
        self.assertEqual(data["pay_day"], self.payment.pay_day)
        self.assertEqual(data["value"], self.payment.value)
        self.assertEqual(data["status"], self.payment.status)


class SerializerCoachTestCase(TestCase):
    def setUp(self):
        self.coach = Coach(
            name="test coach",
            specialty="test specialty",
            email="testemailcoach@mail.com",
            phone="21 99999-9999",
        )
        self.coach_serializer = CoachSerializer(instance=self.coach)

    def test_verify_Coach_fields_serialized(self):
        """Test to verify if Coach fields are serialized"""
        data = self.coach_serializer.data
        self.assertEqual(
            set(data.keys()), set(["id", "name", "specialty", "email", "phone"])
        )

    def test_verify_content_Coach_fields_serializer(self):
        """Test to verify the content into the fields Coach serializer"""
        data = self.coach_serializer.data
        self.assertEqual(data["name"], self.coach.name)
        self.assertEqual(data["specialty"], self.coach.specialty)
        self.assertEqual(data["email"], self.coach.email)
        self.assertEqual(data["phone"], self.coach.phone)
