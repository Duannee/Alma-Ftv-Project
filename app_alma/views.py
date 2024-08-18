from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
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


class CreateAccountView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def perform_create(self, serializer):
    #     username = serializer.validated_data.get("username")
    #     email = serializer.validated_data.get("email")

    #     if Account.objects.filter(username=username).exists():
    #         raise ValidationError(
    #             {
    #                 "error": "An account with this username already exists, please choose another."
    #             }
    #         )

    #     if Account.objects.filter(email=email).exists():
    #         raise ValidationError(
    #             {
    #                 "error": "An account with this email already exists, please choose another."
    #             }
    #         )

    #     return serializer.save()


class ListAccountView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyAccountView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
