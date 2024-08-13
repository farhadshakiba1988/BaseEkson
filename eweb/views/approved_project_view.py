from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from eweb.models import ApprovedProject


class ApprovedProjectListView(ListView):
    model = ApprovedProject
    template_name = 'approvedproject_list.html'
    context_object_name = 'approved_projects'


class ApprovedProjectDetailView(DetailView):
    model = ApprovedProject
    template_name = 'approvedproject_detail.html'
    context_object_name = 'approved_project'


class ApprovedProjectCreateView(CreateView):
    model = ApprovedProject
    fields = ['project', 'approval_date', 'approved_by']
    template_name = 'approvedproject_form.html'


class ApprovedProjectUpdateView(UpdateView):
    model = ApprovedProject
    fields = ['project', 'approval_date', 'approved_by']
    template_name = 'approvedproject_form.html'


class ApprovedProjectDeleteView(DeleteView):
    model = ApprovedProject
    template_name = 'approvedproject_confirm_delete.html'
    success_url = '/approvedprojects/'
