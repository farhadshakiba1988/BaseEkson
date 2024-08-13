from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from eweb.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['project_name', 'description', 'start_date', 'end_date', 'expert']
    template_name = 'project_form.html'

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['project_name', 'description', 'start_date', 'end_date', 'expert']
    template_name = 'project_form.html'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = '/projects/'
