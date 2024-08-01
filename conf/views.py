from django.shortcuts import render
from conf.models.bazargani_lead import LeadInfo
from conf.models.crm_entry import CRMEntry
from conf.models.lead import Lead


# Create your views here.
def home(request):
    # دریافت داده‌های مدل Lead
    leads = Lead.objects.all()

    # دریافت داده‌های مدل CommercialLead
    commercial_leads = LeadInfo.objects.all()

    context = {
        'leads': leads,
        'commercial_leads': commercial_leads,
    }
    return render(request, 'index9.html', context)


def crm_list_view(request):
    entries = CRMEntry.objects.all()
    return render(request, 'index9.html', {'entries': entries})


def report_all(request):
    leads = Lead.objects.all()
    return render(request, 'components/reports/report_all.html',
                  {'leads': leads})


def test1_view(request):
    leads = LeadInfo.objects.all()
    return render(request, 'test1.html', {'leads': leads})
