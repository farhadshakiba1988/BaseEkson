from django.shortcuts import render
from conf.models.bazargani_lead import LeadInfo
from conf.models.lead import Lead
from conf.models.task_report import TaskReport


# Create your views here.
def home(request):
    leads = Lead.objects.all()
    commercial_leads = LeadInfo.objects.all()
    task = TaskReport.objects.all()

    ctx = {
        'leads': leads,
        'commercial_leads': commercial_leads,
        'task': task,
    }
    return render(request, 'index9.html', ctx)


def report_all(request):
    leads = Lead.objects.all()
    return render(request, 'components/reports/report_all.html',
                  {'leads': leads})


def bazarghani_report(request):
    commercial_leads = LeadInfo.objects.all()
    return render(request, 'bazargani.html',
                  {'commercial_leads': commercial_leads})


