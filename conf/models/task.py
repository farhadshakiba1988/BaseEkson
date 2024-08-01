from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                    related_name='assigned_tasks')
    assignment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
