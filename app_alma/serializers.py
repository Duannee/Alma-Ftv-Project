from rest_framework import serializers, status
from .models import Student, StudentProfile, Payment, Coach, User
from rest_framework.exceptions import ValidationError


class UserSerializerPostPutPatch(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
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

    def get_field_names(self, declared_fields, info):
        field_names = super().get_field_names(declared_fields, info)
        model_fields = set(self.Meta.model._meta.get_fields())
        model_field_names = {field.name for field in model_fields}

        for field in self.initial_data.keys():
            if field not in model_field_names:
                raise ValidationError(
                    {field: f"this field '{field}' does not exists."},
                    code=status.HTTP_400_BAD_REQUEST,
                )

        return field_names


class UserSerializerGetDelete(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }


class StudentSerializerPostPathPut(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

    def get_field_names(self, declared_fields, info):
        field_names = super().get_field_names(declared_fields, info)
        model_fields = set(self.Meta.model._meta.get_fields())
        model_field_names = {field.name for field in model_fields}

        for field in self.initial_data.keys():
            if field not in model_field_names:
                raise ValidationError(
                    {field: f"this field '{field}' does not exists."},
                    code=status.HTTP_400_BAD_REQUEST,
                )

        return field_names


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

    def get_field_names(self, declared_fields, info):
        field_names = super().get_field_names(declared_fields, info)
        model_fields = set(self.Meta.model._meta.get_fields())
        model_field_names = {field.name for field in model_fields}

        for field in self.initial_data.keys():
            if field not in model_field_names:
                raise ValidationError(
                    {field: f"this field '{field}' does not exists."},
                    code=status.HTTP_400_BAD_REQUEST,
                )

        return field_names


class StudentProfileSerializerGetDelete(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = ["id", "student", "goal", "progress", "feedback"]
        depth = 1
        read_only_fields = ["student"]


class PaymentSerializer(serializers.ModelSerializer):
    # student = StudentSerializer(many=True)

    class Meta:
        model = Payment
        fields = ["id", "student", "pay_day", "value", "status"]
        depth = 1
        read_only_fields = ["student"]


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"
