from django.db import models

from eweb.models import ForeignPurchaseExpert


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    expert = models.ForeignKey(ForeignPurchaseExpert, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.project_name
