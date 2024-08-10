from django.contrib import admin

from web.models import Approval
from web.models.bazargani_lead import LeadInfo
from web.models import CRMNum
from web.models import Lead
from web.models.department import Department
from web.models import CRMEntry
from web.models import Notification
from web.models import Person
from web.models import Sale
from web.models import SalesPersonReport
from web.models import Tag
from web.models import Task
from web.models import TaskReport


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'employee_number', 'job_title', 'department', 'user')
    search_fields = ('full_name', 'employee_number', 'user__username')


admin.site.register(CRMEntry)
admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Lead)
admin.site.register(LeadInfo)
admin.site.register(Approval)
admin.site.register(CRMNum)
admin.site.register(Notification)
admin.site.register(Sale)
admin.site.register(SalesPersonReport)
admin.site.register(Task)
admin.site.register(TaskReport)
admin.site.register(Tag)
