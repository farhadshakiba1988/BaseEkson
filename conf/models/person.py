from django.db import models
from django.contrib.auth.models import User
from conf.models.department import Department


class Person(models.Model):
    id = models.AutoField(
        primary_key=True)  # افزودن فیلد id به عنوان primary key

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='person')
    full_name = models.CharField(max_length=255)
    employee_number = models.CharField(max_length=50, unique=True)
    job_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
