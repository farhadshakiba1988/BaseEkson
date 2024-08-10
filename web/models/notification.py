from django.db import models

from web.models.person import Person


class Notification(models.Model):
    STATUS_CHOICES = [
        ('read', 'Read'),
        ('unread', 'Unread'),
    ]
    notification_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Notification {self.notification_id} - {self.status}"
