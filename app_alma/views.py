from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


from .models import Account, Student, StudentProfile, Payment, Coach
from .serializers import (
    AccountSerializer,
    StudentSerializer,
    StudentProfileSerializer,
    PaymentSerializer,
    CoachSerializer,
)


class ListCreateAccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RetrieveUpdateDestroyAccountView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ListCreateStudentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RetrieveUpdateDestroyStudentView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ListCreateStudentProfileView(ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class RetrieveUpdateDestroyStudentProfileView(RetrieveUpdateDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer


class ListCreatePaymentView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class RetrieveUpdateDestroyPaymentView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ListCreateCoachView(ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class RetrieveUpdateDestroyCoachView(RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
