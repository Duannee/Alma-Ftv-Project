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
    StudentProfileSerializerPostPatchPut,
    StudentProfileSerializerGetDelete,
    PaymentSerializerPostPatchPut,
    PaymentSerializerGetDelete,
    CoachSerializerPostPatchPut,
    CoachSerializerGetDelete,
)
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["User"])
class CreateAccountView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(tags=["User"])
class ListAccountView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


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
    serializer_class = StudentProfileSerializerPostPatchPut

    def perform_create(self, serializer):
        student = get_object_or_404(Student, pk=self.kwargs.get("student_id"))

        if StudentProfile.objects.filter(student=student).exists():
            raise ValidationError(
                {"detail": "A profile with this student ID already exists."}
            )
        return serializer.save(student=student)


@extend_schema(tags=["Student Profile"])
class ListStudentProfileView(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializerGetDelete


@extend_schema(tags=["Student Profile"])
class RetrieveStudentProfileView(RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializerGetDelete


@extend_schema(tags=["Student Profile"])
class UpdateStudentProfileView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializerPostPatchPut


@extend_schema(tags=["Student Profile"])
class DeleteStudentProfileView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializerGetDelete


@extend_schema(tags=["Payment"])
class CreatePaymentView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PaymentSerializerPostPatchPut

    def perform_create(self, serializer):
        student_payment = get_object_or_404(Student, pk=self.kwargs.get("student_id"))

        if Payment.objects.filter(student=student_payment).exists():
            raise ValidationError(
                {"error": "Already exists a payment for this student"}
            )
        return serializer.save(student=student_payment)


@extend_schema(tags=["Payment"])
class ListPaymentView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializerGetDelete


@extend_schema(tags=["Payment"])
class RetrievePaymentView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializerGetDelete


@extend_schema(tags=["Payment"])
class UpdatePaymentView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializerPostPatchPut


@extend_schema(tags=["Payment"])
class DeletePaymentView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializerGetDelete


@extend_schema(tags=["Coach"])
class CreateCoachView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializerPostPatchPut


@extend_schema(tags=["Coach"])
class ListCoachView(ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializerGetDelete


@extend_schema(tags=["Coach"])
class RetrieveCoachView(RetrieveAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializerGetDelete


@extend_schema(tags=["Coach"])
class UpdateCoachView(UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializerPostPatchPut


@extend_schema(tags=["Coach"])
class DeleteCoachView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coach.objects.all()
    serializer_class = CoachSerializerGetDelete
