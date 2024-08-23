from rest_framework import serializers, status
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


class StudentSerializerGetDelete(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentProfileSerializerPostPatchPut(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = ["id", "student", "goal", "progress", "feedback"]
        depth = 1
        read_only_fields = ["student"]


class StudentProfileSerializerGetDelete(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = ["id", "student", "goal", "progress", "feedback"]
        depth = 1
        read_only_fields = ["student"]


class PaymentSerializerPostPatchPut(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ["id", "student", "pay_day", "value", "status"]
        depth = 1
        read_only_fields = ["student"]


class PaymentSerializerGetDelete(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ["id", "student", "pay_day", "value", "status"]
        depth = 1
        read_only_fields = ["student"]


class CoachSerializerPostPatchPut(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"


class CoachSerializerGetDelete(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"
