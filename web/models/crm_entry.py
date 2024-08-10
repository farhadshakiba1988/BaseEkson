from django.db import models


class CRMEntry(models.Model):
    crm_no = models.IntegerField()
    expert_name = models.CharField(max_length=255)
    expert_email = models.EmailField()
    company_phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    delivery_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.crm_no} - {self.expert_name}"
