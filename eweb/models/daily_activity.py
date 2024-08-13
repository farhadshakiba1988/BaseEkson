from django.db import models

from eweb.models import ForeignPurchaseExpert


class DailyActivity(models.Model):
    date = models.DateField()
    description = models.TextField()
    expert = models.ForeignKey(ForeignPurchaseExpert, on_delete=models.CASCADE, related_name='daily_activities')

    def __str__(self):
        return f"Activity on {self.date} by {self.expert}"
