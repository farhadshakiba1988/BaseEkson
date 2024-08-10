from django.urls import path

from web.views.bazarghani_report_views import LeadInfo
from .Views.index_views import Farhad
from .Views.invoice_views import Invoice
from web.views.report_all_views import Lead

app_name = 'conf'
urlpatterns = [
    path('', Farhad.as_view(), name='farhad'),
    path('invoice/', Invoice.as_view(), name='invoice'),
    path('report_all/', Lead.as_view(), name='report_all'),
    path('bazarghani_report/', LeadInfo.as_view(),
         name='bazarghani_report'),
]
