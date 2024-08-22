from django.db import models
from django.contrib.auth.models import AbstractUser


class PaymentStatusChoices(models.TextChoices):
    UP_TO_DATE = "Up to date"
    PENDING = "Pending"
    LATE = "Late"


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.TextField(max_length=255)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.TextField(max_length=20)
    category = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    goal = models.TextField(max_length=255)
    progress = models.TextField(max_length=255)
    feedback = models.TextField(max_length=255)


class Payment(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    pay_day = models.DateField()
    value = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.CharField(
        max_length=20,
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.UP_TO_DATE,
    )

    def __str__(self) -> str:
        return f"{self.student_id.name} - {self.pay_day}"


class Coach(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.TextField(max_length=20)

    def __str__(self) -> str:
        return self.nome
