from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from eweb.models import ContractCompany


class ContractCompanyListView(ListView):
    model = ContractCompany
    template_name = 'contractcompany_list.html'
    context_object_name = 'contract_companies'

class ContractCompanyDetailView(DetailView):
    model = ContractCompany
    template_name = 'contractcompany_detail.html'
    context_object_name = 'contract_company'

class ContractCompanyCreateView(CreateView):
    model = ContractCompany
    fields = ['company_name', 'contact_person', 'phone_number', 'email', 'address']
    template_name = 'contractcompany_form.html'

class ContractCompanyUpdateView(UpdateView):
    model = ContractCompany
    fields = ['company_name', 'contact_person', 'phone_number', 'email', 'address']
    template_name = 'contractcompany_form.html'

class ContractCompanyDeleteView(DeleteView):
    model = ContractCompany
    template_name = 'contractcompany_confirm_delete.html'
    success_url = '/contractcompanies/'
