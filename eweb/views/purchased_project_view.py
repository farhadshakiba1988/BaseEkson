from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from eweb.models import PurchasedProject


class PurchasedProjectListView(ListView):
    model = PurchasedProject
    template_name = 'purchasedproject_list.html'
    context_object_name = 'purchased_projects'

class PurchasedProjectDetailView(DetailView):
    model = PurchasedProject
    template_name = 'purchasedproject_detail.html'
    context_object_name = 'purchased_project'

class PurchasedProjectCreateView(CreateView):
    model = PurchasedProject
    fields = ['project', 'purchase_date', 'expert_share']
    template_name = 'purchasedproject_form.html'

class PurchasedProjectUpdateView(UpdateView):
    model = PurchasedProject
    fields = ['project', 'purchase_date', 'expert_share']
    template_name = 'purchasedproject_form.html'

class PurchasedProjectDeleteView(DeleteView):
    model = PurchasedProject
    template_name = 'purchasedproject_confirm_delete.html'
    success_url = '/purchasedprojects/'
