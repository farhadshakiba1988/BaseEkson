from django.contrib import admin

from conf.models.department import Department
from conf.models.crm_entry import CRMEntry
from conf.models.person import Person

admin.site.register(CRMEntry)
admin.site.register(Person)
admin.site.register(Department)
