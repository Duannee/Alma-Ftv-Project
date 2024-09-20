from app_alma.models import User, Student, Payment
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetStudentProfileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="admin", password="admin")
        self.student = Student.objects.create(
            name="test",
            age=21,
            email="test@mail.com",
            phone="99 99999-9999",
            category="test category",
        )
        self.payment = Payment.objects.create(
            student=self.student,
            pay_day="2000-10-20",
            value=300.00,
            status="Pending",
        )

    def test_PAYMENT_GET_request(self):
        """Get request test for Payment"""
        self.url = reverse("payment-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
