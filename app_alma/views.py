from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)


from .models import Account, Student, StudentProfile, Payment, Coach
from .serializers import (
    AccountSerializer,
    StudentSerializer,
    StudentProfileSerializer,
    PaymentSerializer,
    CoachSerializer,
)
from django.shortcuts import get_object_or_404


class ListCreateAccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RetrieveUpdateDestroyAccountView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ListCreateStudentView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RetrieveUpdateDestroyStudentView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CreateStudentProfileView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = StudentProfileSerializer

    def perform_create(self, serializer):
        student = get_object_or_404(Student, pk=self.kwargs.get("student_id"))

        if StudentProfile.objects.filter(student=student).exists():
            raise ValidationError(
                {"detail": "A profile with this student ID already exists."}
            )
        return serializer.save(student=student)


class ListStudentProfileView(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class RetrieveUpdateDestroyStudentProfileView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class CreatePaymentView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        student_payment = get_object_or_404(Student, pk=self.kwargs.get("student_id"))

        if Payment.objects.filter(student=student_payment).exists():
            raise ValidationError(
                {"error": "Already exists a payment for this student"}
            )
        return serializer.save(student=student_payment)


class ListPaymentView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class RetrieveUpdateDestroyPaymentView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ListCreateCoachView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class RetrieveUpdateDestroyCoachView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
