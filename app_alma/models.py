from django.db import models


class PaymentStatusChoices(models.TextChoices):
    UP_TO_DATE = "Up to date"
    PENDING = "Pending"
    LATE = "Late"


class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    email = models.EmailField()
    is_superuser = models.BooleanField()


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    payment_status = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.TextField(max_length=20)
    category = models.CharField(max_length=20, default="")

    def __str__(self) -> str:
        return self.nome


class StudentProfile(models.Model):
    goal = models.TextField(max_length=255)
    progress = models.TextField(max_length=255)
    feedback = models.TextField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Payment(models.Model):
    pay_day = models.DateField()
    value = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.CharField(
        max_length=20,
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.UP_TO_DATE,
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.student_id.name} - {self.pay_day}"


class Coach(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.TextField(max_length=20)

    def __str__(self) -> str:
        return self.nome
