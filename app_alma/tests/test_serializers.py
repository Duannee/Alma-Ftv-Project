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
