from django.shortcuts import render
from django.views import View


class Farhad(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Ekson/../../eweb/templates/index10.html')
