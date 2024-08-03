from django.db import models

from conf.models.person import Person


class Approval(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    ]

    approval_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    related_entity = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    approval_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Approval {self.approval_id} - {self.status}"
