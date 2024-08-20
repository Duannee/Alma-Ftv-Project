from rest_framework import serializers
from .models import Student, StudentProfile, Payment, Coach, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        read_only_fields = ["is_superuser"]
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        return user


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class StudentProfileSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)

    class Meta:
        model = StudentProfile
        fields = ["id", "student", "goal", "progress", "feedback"]
        depth = 1
        read_only_fields = ["student"]


class PaymentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)

    class Meta:
        model = Payment
        fields = ["id", "student", "pay_day", "value", "status"]
        depth = 1
        read_only_fields = ["student"]


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"
