from django.urls import path
from conf import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report_all/', views.report_all, name='report_all'),
    path('test1/', views.test1_view, name='test1_view'),
]
