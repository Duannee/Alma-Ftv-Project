from django.urls import path
from .views import (
    ListCreateAccountView,
    RetrieveUpdateDestroyAccountView,
    ListCreateStudentView,
    RetrieveUpdateDestroyStudentView,
    RetrieveUpdateDestroyStudentProfileView,
    ListCreatePaymentView,
    RetrieveUpdateDestroyPaymentView,
    ListCreateCoachView,
    RetrieveUpdateDestroyCoachView,
    CreateStudentProfileView,
    ListStudentProfileView,
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
]
