from django.shortcuts import render
from django.views import View
from web.models import Lead

class Lead(View):
    def get(self, request, *args, **kwargs):
        leads = Lead.objects.all()
        return render(request, 'components/reports/report_all.html',
                      {'leads': leads})
