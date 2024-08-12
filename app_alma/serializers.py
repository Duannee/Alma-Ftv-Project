from rest_framework import serializers
from .models import Account, Student, StudentProfile, Payment, Coach


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class StudentProfileSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(many=True)

    class Meta:
        model = StudentProfile
        fields = ["id", "goal", "progress", "feedback", "student"]
        depth = 1
        read_only_fields = ["student"]


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"
