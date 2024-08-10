from django.db import models

from web.models.person import Person


class CRMNum(models.Model):
    crm_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    crm_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CRM {self.crm_number}"
