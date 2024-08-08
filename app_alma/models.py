from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    email = models.EmailField()
    is_superuser = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    payment_status = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.TextField(max_length=20)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self) -> str:
        return self.nome


class StudentProfile(models.Model):
    goal = models.TextField(max_length=255)
    progress = models.TextField(max_length=255)
    feedback = models.TextField(max_length=255)
    student_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="profiles"
    )


class Payment(models.Model):
    pay_day = models.DateField()
    value = models.DecimalField(decimal_places=2, max_digits=6)
    status = models.BooleanField()
    student_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="payments"
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


class TrainingSession(models.Model):
    date = models.DateTimeField()
    description = models.TextField(max_length=255)
    place = models.CharField(max_length=15, default="", null=False, blank=False)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="trainings"
    )
    coach_id = models.ForeignKey(
        Coach, on_delete=models.CASCADE, related_name="trainings"
    )
    student_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="trainings"
    )

    def __str__(self) -> str:
        return f"{self.student_id.name} - {self.category_id.name} - {self.date}"
