from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from eweb.models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    fields = ['task_name', 'description', 'assign_date', 'due_date', 'expert', 'project']
    template_name = 'task_form.html'

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['task_name', 'description', 'assign_date', 'due_date', 'expert', 'project']
    template_name = 'task_form.html'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = '/tasks/'
