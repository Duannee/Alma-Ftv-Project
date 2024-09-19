from app_alma.models import Student, User, Payment
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
from decimal import Decimal


class AuthenticationPaymentTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
        self.student = Student.objects.create(
            name="test",
            age=21,
            email="test@mail.com",
            phone="99 99999-9999",
            category="test",
        )

    def test_POST_request_with_authentication(self):
        """Test to verify if Payment POST request with authentication was authorized"""
        self.client.force_authenticate(self.user)
        self.url = reverse("payment-post", kwargs={"student_id": self.student.pk})
        self.data = {
            "student": self.student.id,
            "pay_day": "1980-10-10",
            "value": 999.99,
            "status": "Pending",
        }
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        payment = Payment.objects.get(student=self.student)
        expected_date = datetime.strptime("1980-10-10", "%Y-%m-%d").date()
        self.assertEqual(payment.pay_day, expected_date)
        self.assertEqual(payment.value, Decimal("999.99"))
        self.assertEqual(payment.status, "Pending")
