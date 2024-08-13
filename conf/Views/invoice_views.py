from django.shortcuts import render
from django.views import View


class Invoice(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'NPPD/invoice.html')