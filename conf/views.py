from django.shortcuts import render
from conf.models.crm_entry import CRMEntry
from conf.models.person import Person


# Create your views here.
def home(request):
    persons = [
        {'name': 'John Doe', 'email': 'john@example.com', 'phone': '123456', 'company': 'ABC Corp', 'location': 'USA',
         'date': '2023-04-02', 'status': 'Active', 'id': 1},
        {'name': 'Jane Doe', 'email': 'jane@example.com', 'phone': '654321', 'company': 'XYZ Corp', 'location': 'UK',
         'date': '2023-04-02', 'status': 'Inactive', 'id': 2}
    ]
    context = {
        'persons': persons,
    }
    return render(request, 'index9.html', context)


def crm_list_view(request):
    entries = CRMEntry.objects.all()
    return render(request, 'index9.html', {'entries': entries})

