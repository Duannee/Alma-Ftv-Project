# Generated by Django 5.1 on 2024-08-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_alma', '0002_alter_student_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(max_length=2),
        ),
    ]
