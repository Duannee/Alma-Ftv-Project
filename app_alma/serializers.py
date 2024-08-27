from rest_framework import serializers, request
from .models import Student, StudentProfile, Payment, Coach, User
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }

    def validate(self, data):
        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})
        return data


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, data):
        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})
        return data

    def validate(self, attrs):
        name = attrs.get("name")
        email = attrs.get("email")

        if Student.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                "There is already a student with that name, please choose another one"
            )

        if Student.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "There is already a student with that email, please choose another one"
            )
        return attrs


class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = ["id", "student", "goal", "progress", "feedback"]
        depth = 1
        read_only_fields = ["student"]

    def validate(self, data):
        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})
        return data


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ["id", "student", "pay_day", "value", "status"]
        depth = 1
        read_only_fields = ["student"]

    def validate(self, data):
        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})
        return data


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"

    def validate(self, data):
        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})
        return data

    def validate(self, attrs):
        name = attrs.get("name")
        email = attrs.get("email")

        if Coach.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                "There is already a coach with that name , please choose another one"
            )

        if Coach.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "There is already a coach with that email, please choose another one"
            )

        return attrs
