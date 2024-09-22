from app_alma.models import User, Student, Payment
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GetStudentProfileTestCase(APITestCase):
    fixtures = ["database_prototype.json"]

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.student = Student.objects.get(pk=4)
        self.payment = Payment.objects.get(pk=5)

    def test_PAYMENT_GET_request(self):
        """Get request test for Payment"""
        self.url = reverse("payment-list")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_PAYMENT_GET_ID_request(self):
        """Get ID request test for Payment"""
        self.url = reverse("payment-id-list", kwargs={"pk": self.payment.pk})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
