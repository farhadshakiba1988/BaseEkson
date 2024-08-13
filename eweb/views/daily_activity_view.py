from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from eweb.models import DailyActivity


class DailyActivityListView(ListView):
    model = DailyActivity
    template_name = 'dailyactivity_list.html'
    context_object_name = 'daily_activities'

class DailyActivityDetailView(DetailView):
    model = DailyActivity
    template_name = 'dailyactivity_detail.html'
    context_object_name = 'daily_activity'

class DailyActivityCreateView(CreateView):
    model = DailyActivity
    fields = ['date', 'description', 'expert']
    template_name = 'dailyactivity_form.html'

class DailyActivityUpdateView(UpdateView):
    model = DailyActivity
    fields = ['date', 'description', 'expert']
    template_name = 'dailyactivity_form.html'

class DailyActivityDeleteView(DeleteView):
    model = DailyActivity
    template_name = 'dailyactivity_confirm_delete.html'
    success_url = '/dailyactivities/'
