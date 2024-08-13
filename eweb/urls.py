from django.urls import path

from .urls import *

app_name = 'eweb'
urlpatterns = [
    # ApprovedProject URLs
    path('approvedprojects/', ApprovedProjectListView.as_view(), name='approved_project_list'),
    path('approvedprojects/<int:pk>/', ApprovedProjectDetailView.as_view(), name='approved_project_detail'),
    path('approvedprojects/create/', ApprovedProjectCreateView.as_view(), name='approved_project_create'),
    path('approvedprojects/<int:pk>/update/', ApprovedProjectUpdateView.as_view(), name='approved_project_update'),
    path('approvedprojects/<int:pk>/delete/', ApprovedProjectDeleteView.as_view(), name='approved_project_delete'),

    # ContractCompany URLs
    path('contractcompanies/', ContractCompanyListView.as_view(), name='contract_company_list'),
    path('contractcompanies/<int:pk>/', ContractCompanyDetailView.as_view(), name='contract_company_detail'),
    path('contractcompanies/create/', ContractCompanyCreateView.as_view(), name='contract_company_create'),
    path('contractcompanies/<int:pk>/update/', ContractCompanyUpdateView.as_view(), name='contract_company_update'),
    path('contractcompanies/<int:pk>/delete/', ContractCompanyDeleteView.as_view(), name='contract_company_delete'),

    # DailyActivity URLs
    path('dailyactivities/', DailyActivityListView.as_view(), name='daily_activity_list'),
    path('dailyactivities/<int:pk>/', DailyActivityDetailView.as_view(), name='daily_activity_detail'),
    path('dailyactivities/create/', DailyActivityCreateView.as_view(), name='daily_activity_create'),
    path('dailyactivities/<int:pk>/update/', DailyActivityUpdateView.as_view(), name='daily_activity_update'),
    path('dailyactivities/<int:pk>/delete/', DailyActivityDeleteView.as_view(), name='daily_activity_delete'),

    # ForeignPurchaseExpert URLs
    path('foreignpurchaseexperts/', ForeignPurchaseExpertListView.as_view(), name='foreign_purchase_expert_list'),
    path('foreignpurchaseexperts/<int:pk>/', ForeignPurchaseExpertDetailView.as_view(), name='foreign_purchase_expert_detail'),
    path('foreignpurchaseexperts/create/', ForeignPurchaseExpertCreateView.as_view(), name='foreign_purchase_expert_create'),
    path('foreignpurchaseexperts/<int:pk>/update/', ForeignPurchaseExpertUpdateView.as_view(), name='foreign_purchase_expert_update'),
    path('foreignpurchaseexperts/<int:pk>/delete/', ForeignPurchaseExpertDeleteView.as_view(), name='foreign_purchase_expert_delete'),

    # Project URLs
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    # PurchasedProject URLs
    path('purchasedprojects/', PurchasedProjectListView.as_view(), name='purchased_project_list'),
    path('purchasedprojects/<int:pk>/', PurchasedProjectDetailView.as_view(), name='purchased_project_detail'),
    path('purchasedprojects/create/', PurchasedProjectCreateView.as_view(), name='purchased_project_create'),
    path('purchasedprojects/<int:pk>/update/', PurchasedProjectUpdateView.as_view(), name='purchased_project_update'),
    path('purchasedprojects/<int:pk>/delete/', PurchasedProjectDeleteView.as_view(), name='purchased_project_delete'),

    # Task URLs
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]