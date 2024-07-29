from django.db import models

from conf.models.department import Department


class Person(models.Model):
    full_name = models.CharField(max_length=255)
    employee_number = models.CharField(max_length=50, unique=True)
    job_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
