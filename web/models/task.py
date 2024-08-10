from django.db import models
from django.contrib.auth.models import User

from web.models.person import Person
from web.models.tag import Tag


class Task(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('cancelled', 'Cancelled'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    person = models.ForeignKey(Person, related_name='tasks', on_delete=models.CASCADE)

    assigned_to = models.ForeignKey(Person, related_name='assigned_tasks', on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    progress = models.IntegerField(default=0)  # progress percentage
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    team_members = models.ManyToManyField(User, related_name='tasks')
    tags = models.ManyToManyField(Tag, related_name='tasks')
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                    related_name='assigned_tasks')
    assignment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
