from django.urls import path
from conf import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report_all/', views.report_all, name='report_all'),
    path('bazarghani_report/', views.bazarghani_report, name='bazarghani_report'),
]
