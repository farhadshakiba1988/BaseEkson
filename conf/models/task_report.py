from django.db import models


class TaskReport(models.Model):
    STATUS_CHOICES = (
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('success', 'Success'),
        ('danger', 'Danger'),
        ('warning', 'Warning'),
        ('info', 'Info'),
        ('pink', 'Pink'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_status_class(self):
        # تابعی برای بازگرداندن کلاس CSS مناسب بر اساس وضعیت
        status_class_mapping = {
            'primary': 'text-primary',
            'secondary': 'text-secondary',
            'success': 'text-success',
            'danger': 'text-danger',
            'warning': 'text-warning',
            'info': 'text-info',
            'pink': 'text-pink-500',
        }
        return status_class_mapping.get(self.status, 'text-gray-500')
