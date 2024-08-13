from django.db import models

from eweb.models import ForeignPurchaseExpert
from eweb.models import Project


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    assign_date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    expert = models.ForeignKey(ForeignPurchaseExpert, on_delete=models.CASCADE, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.task_name
