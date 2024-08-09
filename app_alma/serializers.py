from rest_framework import serializers
from .models import (
    Account,
    Category,
    Student,
    StudentProfile,
    Payment,
    Coach,
    TrainingSession,
)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Student
        fields = "__all__"


class StudentProfileSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)

    class Meta:
        model = StudentProfile
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)

    class Meta:
        model = Payment
        fields = "__all__"


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"
