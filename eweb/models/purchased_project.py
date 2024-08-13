from django.db import models

from eweb.models import Project


class PurchasedProject(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='purchased_project')
    purchase_date = models.DateField()
    expert_share = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Purchased: {self.project.project_name} with share {self.expert_share}%"
