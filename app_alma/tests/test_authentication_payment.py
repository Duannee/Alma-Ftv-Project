from app_alma.models import Student, User, Payment
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
from decimal import Decimal


class AuthenticationPaymentTestCase(APITestCase):
    fixtures = ["database_prototype.json"]

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.student = Student.objects.get(pk=4)
        self.client.force_authenticate(self.user)

    def test_POST_request_with_authentication(self):
        """Test to verify if Payment POST request with authentication was authorized"""
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

    def test_PATCH_request_with_authentication(self):
        """Test to verify if Payment PATCH request with authentication was authorized"""
        self.payment = Payment.objects.get(pk=5)
        self.url = reverse("payment-patch", kwargs={"pk": self.payment.pk})
        self.data = {
            "pay_day": "1980-10-10",
            "value": 999.99,
            "status": "Pending",
        }
        response = self.client.patch(self.url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payment.refresh_from_db()
        expected_date = datetime.strptime("1980-10-10", "%Y-%m-%d").date()
        self.assertEqual(self.payment.pay_day, expected_date)
        self.assertEqual(self.payment.value, Decimal("999.99"))
        self.assertEqual(self.payment.status, "Pending")

    def test_DELETE_request_with_authentication(self):
        """Test to verify if Payment DELETE request with authentication was authorized"""
        self.payment = Payment.objects.get(pk=5)
        self.url = reverse("payment-delete", kwargs={"pk": self.payment.pk})
        self.assertTrue(Payment.objects.filter(pk=self.payment.pk).exists())
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Payment.DoesNotExist):
            Payment.objects.get(pk=self.payment.pk)
