from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)


from .models import User, Student, StudentProfile, Payment, Coach
from .serializers import (
    UserSerializer,
    StudentSerializer,
    StudentProfileSerializer,
    PaymentSerializer,
    CoachSerializer,
)
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(create=extend_schema(tags=["User"]))
class CreateAccountView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListAccountView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveAccountView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateAccountView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteAccountView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateStudentView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ListStudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RetrieveStudentView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UpdateStudentView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudentView(DestroyAPIView):
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


class RetrieveStudentProfileView(RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class UpdateStudentProfileView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class DeleteStudentProfileView(DestroyAPIView):
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


class RetrievePaymentView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class UpdatePaymentView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class DeletePaymentView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CreateCoachView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class ListCoachView(ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class RetrieveCoachView(RetrieveAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class UpdateCoachView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class DeleteCoachView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
