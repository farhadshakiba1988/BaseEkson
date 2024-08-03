from django.contrib import admin

from conf.models.approval import Approval
from conf.models.bazargani_lead import LeadInfo
from conf.models.crm_num import CRMNum
from conf.models.lead import Lead
from conf.models.department import Department
from conf.models.crm_entry import CRMEntry
from conf.models.notification import Notification
from conf.models.person import Person
from conf.models.sales import Sale
from conf.models.salespersonreport import SalesPersonReport
from conf.models.task import Task
from conf.models.task_report import TaskReport


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
