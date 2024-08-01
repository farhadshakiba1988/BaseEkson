from django.contrib import admin

from conf.models.bazargani_lead import LeadInfo
from conf.models.lead import Lead
from conf.models.department import Department
from conf.models.crm_entry import CRMEntry
from conf.models.person import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'employee_number', 'job_title', 'department', 'user')
    search_fields = ('full_name', 'employee_number', 'user__username')


admin.site.register(CRMEntry)
admin.site.register(Person)
admin.site.register(Department)
admin.site.register(Lead)
admin.site.register(LeadInfo)
