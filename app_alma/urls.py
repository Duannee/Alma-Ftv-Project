from django.urls import path
from .views import (
    ListCreateAccountView,
    RetrieveUpdateDestroyAccountView,
    ListCreateStudentView,
    RetrieveUpdateDestroyStudentView,
    RetrieveUpdateDestroyStudentProfileView,
    RetrieveUpdateDestroyPaymentView,
    ListCreateCoachView,
    RetrieveUpdateDestroyCoachView,
    CreateStudentProfileView,
    ListStudentProfileView,
    CreatePaymentView,
    ListPaymentView,
)

urlpatterns = [
    # Account routes
    path("account/create/", ListCreateAccountView.as_view()),
    path("account/list/", ListCreateAccountView.as_view()),
    path("account/<int:pk>/retrieve/", RetrieveUpdateDestroyAccountView.as_view()),
    path("account/<int:pk>/update/", RetrieveUpdateDestroyAccountView.as_view()),
    path("account/<int:pk>/delete/", RetrieveUpdateDestroyAccountView.as_view()),
    # Students routes
    path("student/create/", ListCreateStudentView.as_view()),
    path("student/list/", ListCreateStudentView.as_view()),
    path("student/<int:pk>/retrieve/", RetrieveUpdateDestroyStudentView.as_view()),
    path("student/<int:pk>/update/", RetrieveUpdateDestroyStudentView.as_view()),
    path("student/<int:pk>/delete/", RetrieveUpdateDestroyStudentView.as_view()),
    # Student profile routes
    path(
        "student/<int:student_id>/profile/create/", CreateStudentProfileView.as_view()
    ),
    path("student_profile/list/", ListStudentProfileView.as_view()),
    path(
        "student_profile/<int:pk>/retrieve/",
        RetrieveUpdateDestroyStudentProfileView.as_view(),
    ),
    path(
        "student_profile/<int:pk>/update/",
        RetrieveUpdateDestroyStudentProfileView.as_view(),
    ),
    path(
        "student_profile/<int:pk>/delete/",
        RetrieveUpdateDestroyStudentProfileView.as_view(),
    ),
    # Payment routes
    path("payment/<int:student_id>/student/create/", CreatePaymentView.as_view()),
    path("payment/list/", ListPaymentView.as_view()),
    path("payment/<int:pk>/retrieve/", RetrieveUpdateDestroyPaymentView.as_view()),
    path("payment/<int:pk>/update/", RetrieveUpdateDestroyPaymentView.as_view()),
    path("payment/<int:pk>/delete/", RetrieveUpdateDestroyPaymentView.as_view()),
    # Coach routes
    path("coach/create/", ListCreateCoachView.as_view()),
    path("coach/list/", ListCreateCoachView.as_view()),
    path("coach/<int:pk>/retrieve/", RetrieveUpdateDestroyCoachView.as_view()),
    path("coach/<int:pk>/update/", RetrieveUpdateDestroyCoachView.as_view()),
    path("coach/<int:pk>/delete/", RetrieveUpdateDestroyCoachView.as_view()),
]
