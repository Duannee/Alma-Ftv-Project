from django.urls import path
from rest_framework_simplejwt import views
from .views import (
    CreateAccountView,
    ListAccountView,
    RetrieveAccountView,
    UpdateAccountView,
    DeleteAccountView,
    CreateStudentView,
    ListStudentView,
    RetrieveStudentView,
    UpdateStudentView,
    DeleteStudentView,
    CreateStudentProfileView,
    ListStudentProfileView,
    RetrieveStudentProfileView,
    UpdateStudentProfileView,
    DeleteStudentProfileView,
    CreatePaymentView,
    ListPaymentView,
    RetrievePaymentView,
    UpdatePaymentView,
    DeletePaymentView,
    CreateCoachView,
    ListCoachView,
    RetrieveCoachView,
    UpdateCoachView,
    DeleteCoachView,
)

urlpatterns = [
    # Token routes
    path("token/", views.TokenObtainPairView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
    # User routes
    path(
        "user/create/",
        CreateAccountView.as_view(),
    ),
    path("user/list/", ListAccountView.as_view()),
    path("user/<int:pk>/retrieve/", RetrieveAccountView.as_view()),
    path(
        "user/<int:pk>/update/",
        UpdateAccountView.as_view(),
    ),
    path(
        "user/<int:pk>/delete/",
        DeleteAccountView.as_view(),
    ),
    # Students routes
    path("student/create/", CreateStudentView.as_view(), name="student-post"),
    path("student/list/", ListStudentView.as_view()),
    path("student/<int:pk>/retrieve/", RetrieveStudentView.as_view()),
    path("student/<int:pk>/update/", UpdateStudentView.as_view()),
    path("student/<int:pk>/delete/", DeleteStudentView.as_view()),
    # Student profile routes
    path(
        "student/<int:student_id>/profile/create/", CreateStudentProfileView.as_view()
    ),
    path("student_profile/list/", ListStudentProfileView.as_view()),
    path(
        "student_profile/<int:pk>/retrieve/",
        RetrieveStudentProfileView.as_view(),
    ),
    path(
        "student_profile/<int:pk>/update/",
        UpdateStudentProfileView.as_view(),
    ),
    path(
        "student_profile/<int:pk>/delete/",
        DeleteStudentProfileView.as_view(),
    ),
    # Payment routes
    path("payment/<int:student_id>/student/create/", CreatePaymentView.as_view()),
    path("payment/list/", ListPaymentView.as_view()),
    path("payment/<int:pk>/retrieve/", RetrievePaymentView.as_view()),
    path("payment/<int:pk>/update/", UpdatePaymentView.as_view()),
    path("payment/<int:pk>/delete/", DeletePaymentView.as_view()),
    # Coach routes
    path("coach/create/", CreateCoachView.as_view()),
    path("coach/list/", ListCoachView.as_view()),
    path("coach/<int:pk>/retrieve/", RetrieveCoachView.as_view()),
    path("coach/<int:pk>/update/", UpdateCoachView.as_view()),
    path("coach/<int:pk>/delete/", DeleteCoachView.as_view()),
]
