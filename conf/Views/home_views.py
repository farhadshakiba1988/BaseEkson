from django.shortcuts import render
from django.views import View

from web.models import Lead, LeadInfo, TaskReport


class Home(View):
    def get(self, request, *args, **kwargs):
        leads = Lead.objects.all()
        commercial_leads = LeadInfo.objects.all()
        task = TaskReport.objects.all()

        ctx = {
            'leads': leads,
            'commercial_leads': commercial_leads,
            'task': task,
        }
        return render(request, 'NPPD/index9.html', ctx)
