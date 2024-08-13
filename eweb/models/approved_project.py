from django.db import models

from eweb.models import Project


class ApprovedProject(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='approved_project')
    approval_date = models.DateField()
    approved_by = models.CharField(max_length=100)

    def __str__(self):
        return f"Approved: {self.project.project_name}"
