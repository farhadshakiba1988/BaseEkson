from django.db import models
from django.db.models import Sum

from web.models.person import Person


# مدل SalesPersonReport برای مدیریت گزارش فروش فردی

class SalesPersonReport(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='sales_report')

    def __str__(self):
        return f"Sales Report for {self.person}"

    def total_sales_amount(self):
        return self.person.sales.aggregate(total=Sum('amount'))['total'] or 0
