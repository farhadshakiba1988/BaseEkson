from django.db import models
from django.contrib.auth.models import User

from conf.models.department import Department


class Person(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('employee', 'Employee'),
        ('vendor', 'Vendor'),
        ('manager', 'Manager'),
    ]
    id = models.AutoField(primary_key=True)  # افزودن فیلد id به عنوان primary key

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='person')
    full_name = models.CharField(max_length=255)
    employee_number = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.full_name
