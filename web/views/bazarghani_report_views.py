from django.shortcuts import render
from django.views import View
from web.models import LeadInfo


class LeadInfo(View):
    def get(self, request, *args, **kwargs):
        commercial_leads = LeadInfo.objects.all()
        return render(request, 'bazargani.html',
                      {'commercial_leads': commercial_leads})
