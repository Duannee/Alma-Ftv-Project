from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import (
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
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["User"])
class CreateAccountView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["User"])
class ListAccountView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get("username")
        if username is not None:
            queryset = queryset.filter(username__icontains=username)
        return queryset


@extend_schema(tags=["User"])
class RetrieveAccountView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["User"])
class UpdateAccountView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def partial_update(self, request, *args, **kwargs):
        invalid_fields = [
            key for key in request.data if key not in self.serializer_class().fields
        ]

        if invalid_fields:
            raise ValidationError({"invalid_fields": invalid_fields})

        return super().partial_update(request, *args, **kwargs)


@extend_schema(tags=["User"])
class DeleteAccountView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["Student"])
class CreateStudentView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@extend_schema(tags=["Student"])
class ListStudentView(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()

        name = self.request.query_params.get("name")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


@extend_schema(tags=["Student"])
class RetrieveStudentView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@extend_schema(tags=["Student"])
class UpdateStudentView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def partial_update(self, request, *args, **kwargs):
        invalid_fields = [
            key for key in request.data if key not in self.serializer_class().fields
        ]

        if invalid_fields:
            raise ValidationError({"invalid_fields": invalid_fields})

        return super().partial_update(request, *args, **kwargs)


@extend_schema(tags=["Student"])
class DeleteStudentView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@extend_schema(tags=["Student Profile"])
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


@extend_schema(tags=["Student Profile"])
class ListStudentProfileView(ListAPIView):

    serializer_class = StudentProfileSerializer

    def get_queryset(self):
        queryset = StudentProfile.objects.all()
        student = self.request.query_params.get("student")
        if student is not None:
            queryset = queryset.filter(student__name__icontains=student)
        return queryset


@extend_schema(tags=["Student Profile"])
class RetrieveStudentProfileView(RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


@extend_schema(tags=["Student Profile"])
class UpdateStudentProfileView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    def partial_update(self, request, *args, **kwargs):
        invalid_fields = [
            key for key in request.data if key not in self.serializer_class().fields
        ]

        if invalid_fields:
            raise ValidationError({"invalid_fields": invalid_fields})

        return super().partial_update(request, *args, **kwargs)


@extend_schema(tags=["Student Profile"])
class DeleteStudentProfileView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


@extend_schema(tags=["Payment"])
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


@extend_schema(tags=["Payment"])
class ListPaymentView(ListAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = Payment.objects.all()
        student = self.request.query_params.get("student")
        if student is not None:
            queryset = queryset.filter(student__name__icontains=student)
        return queryset


@extend_schema(tags=["Payment"])
class RetrievePaymentView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@extend_schema(tags=["Payment"])
class UpdatePaymentView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def partial_update(self, request, *args, **kwargs):
        invalid_fields = [
            key for key in request.data if key not in self.serializer_class().fields
        ]

        if invalid_fields:
            raise ValidationError({"invalid_fields": invalid_fields})

        return super().partial_update(request, *args, **kwargs)


@extend_schema(tags=["Payment"])
class DeletePaymentView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


@extend_schema(tags=["Coach"])
class CreateCoachView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


@extend_schema(tags=["Coach"])
class ListCoachView(ListAPIView):
    serializer_class = CoachSerializer

    def get_queryset(self):
        queryset = Coach.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset


@extend_schema(tags=["Coach"])
class RetrieveCoachView(RetrieveAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


@extend_schema(tags=["Coach"])
class UpdateCoachView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

    def partial_update(self, request, *args, **kwargs):
        invalid_fields = [
            key for key in request.data if key not in self.serializer_class().fields
        ]

        if invalid_fields:
            raise ValidationError({"invalid_fields": invalid_fields})

        return super().partial_update(request, *args, **kwargs)


@extend_schema(tags=["Coach"])
class DeleteCoachView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
