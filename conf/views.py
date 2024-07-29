from django.shortcuts import render
from conf.models.crm_entry import CRMEntry


# Create your views here.
def home(request):
    return render(request, 'index9.html')


def crm_list_view(request):
    entries = CRMEntry.objects.all()
    return render(request, 'test1.html', {'entries': entries})
