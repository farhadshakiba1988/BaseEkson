from django.db import models
from django.contrib.auth.models import User

from conf.models.person import Person


class Task(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('cancelled', 'Cancelled'),
    ]
    task_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Person, related_name='assigned_tasks', on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    description = models.TextField()
    title = models.CharField(max_length=100)
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                    related_name='assigned_tasks')
    assignment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
