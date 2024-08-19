from django.contrib import admin
from .models import User, Student, StudentProfile, Payment, Coach

admin.site.register(User)
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Payment)
admin.site.register(Coach)
