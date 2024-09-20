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
    path("user/list/", ListAccountView.as_view(), name="user-list"),
    path("user/<int:pk>/retrieve/", RetrieveAccountView.as_view(), name="user-id-list"),
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
    path("student/list/", ListStudentView.as_view(), name="student-list"),
    path(
        "student/<int:pk>/retrieve/",
        RetrieveStudentView.as_view(),
        name="student-id-list",
    ),
    path(
        "student/<int:pk>/update/", UpdateStudentView.as_view(), name="student-update"
    ),
    path(
        "student/<int:pk>/delete/", DeleteStudentView.as_view(), name="student-delete"
    ),
    # Student profile routes
    path(
        "student/<int:student_id>/profile/create/",
        CreateStudentProfileView.as_view(),
        name="student-profile-post",
    ),
    path(
        "student_profile/list/",
        ListStudentProfileView.as_view(),
        name="student-profile-list",
    ),
    path(
        "student_profile/<int:pk>/retrieve/",
        RetrieveStudentProfileView.as_view(),
        name="student-profile-id-list",
    ),
    path(
        "student_profile/<int:pk>/update/",
        UpdateStudentProfileView.as_view(),
        name="student-profile-patch",
    ),
    path(
        "student_profile/<int:pk>/delete/",
        DeleteStudentProfileView.as_view(),
        name="student-profile-delete",
    ),
    # Payment routes
    path(
        "payment/<int:student_id>/student/create/",
        CreatePaymentView.as_view(),
        name="payment-post",
    ),
    path("payment/list/", ListPaymentView.as_view(), name="payment-list"),
    path("payment/<int:pk>/retrieve/", RetrievePaymentView.as_view()),
    path("payment/<int:pk>/update/", UpdatePaymentView.as_view(), name="payment-patch"),
    path(
        "payment/<int:pk>/delete/", DeletePaymentView.as_view(), name="payment-delete"
    ),
    # Coach routes
    path("coach/create/", CreateCoachView.as_view(), name="coach-post"),
    path("coach/list/", ListCoachView.as_view()),
    path("coach/<int:pk>/retrieve/", RetrieveCoachView.as_view()),
    path("coach/<int:pk>/update/", UpdateCoachView.as_view(), name="coach-update"),
    path("coach/<int:pk>/delete/", DeleteCoachView.as_view(), name="coach-delete"),
]
