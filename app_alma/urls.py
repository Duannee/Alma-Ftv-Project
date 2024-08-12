from django.urls import path
from .views import (
    ListCreateAccountView,
    RetrieveUpdateDestroyAccountView,
    ListCreateStudentView,
    RetrieveUpdateDestroyStudentView,
    RetrieveUpdateDestroyStudentProfileView,
    RetrieveUpdateDestroyPaymentView,
    # ListCreateCoachView,
    # RetrieveUpdateDestroyCoachView,
    CreateStudentProfileView,
    ListStudentProfileView,
    CreatePaymentView,
    ListPaymentView,
)

urlpatterns = [
    path("account/", ListCreateAccountView.as_view()),
    path("account/", RetrieveUpdateDestroyAccountView.as_view()),
    path("account/<int:pk>/", RetrieveUpdateDestroyAccountView.as_view()),
    path("student/", ListCreateStudentView.as_view()),
    path("student/<int:pk>/", RetrieveUpdateDestroyStudentView.as_view()),
    path("student/<int:student_id>/profile/", CreateStudentProfileView.as_view()),
    path("student_profile/", ListStudentProfileView.as_view()),
    path(
        "student_profile/<int:pk>/", RetrieveUpdateDestroyStudentProfileView.as_view()
    ),
    path("payment/<int:student_id>/student", CreatePaymentView.as_view()),
    path("payment/", ListPaymentView.as_view()),
    path("payment/<int:pk>/", RetrieveUpdateDestroyPaymentView.as_view()),
]
