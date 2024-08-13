from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from eweb.models import ForeignPurchaseExpert


class ForeignPurchaseExpertListView(ListView):
    model = ForeignPurchaseExpert
    template_name = 'foreignpurchaseexpert_list.html'
    context_object_name = 'foreign_purchase_experts'

class ForeignPurchaseExpertDetailView(DetailView):
    model = ForeignPurchaseExpert
    template_name = 'foreignpurchaseexpert_detail.html'
    context_object_name = 'foreign_purchase_expert'

class ForeignPurchaseExpertCreateView(CreateView):
    model = ForeignPurchaseExpert
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'position']
    template_name = 'foreignpurchaseexpert_form.html'

class ForeignPurchaseExpertUpdateView(UpdateView):
    model = ForeignPurchaseExpert
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'position']
    template_name = 'foreignpurchaseexpert_form.html'

class ForeignPurchaseExpertDeleteView(DeleteView):
    model = ForeignPurchaseExpert
    template_name = 'foreignpurchaseexpert_confirm_delete.html'
    success_url = '/foreignpurchaseexperts/'
