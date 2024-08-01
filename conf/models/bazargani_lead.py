from django.db import models


class LeadInfo(models.Model):  # تغییر نام مدل به LeadInfo
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[('won', 'سرنخ موفق'),
                                                      ('lost', 'سرنخ ناموفق')])
    additional_info_1 = models.TextField(null=True, blank=True)
    additional_info_2 = models.TextField(null=True, blank=True)
    approval_status = models.CharField(max_length=20,
                                       choices=[('approved', 'تایید شده'),
                                                ('rejected', 'رد شده'),
                                                ('pending', 'در انتظار')],
                                       default='pending')

    def __str__(self):
        return self.name
