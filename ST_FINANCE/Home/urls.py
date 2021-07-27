from django.urls import path
from . import views


urlpatterns = [
    path('', views.resource_view,name="Home"),
    path('FTE/', views.FTE_plan_func,name='FTE_page'),
    path('Admin/', views.admin_view,name='Admin_page'),
    path('Project_SLA/', views.FTE_plan_func,name='Project_SLA_page'),
    path('Program_SLA/', views.FTE_plan_func,name='Program_SLA_page'),
    path('Project_ADD/',views.projectADD_func,name='project_add_page'),
    path('Program_ADD/',views.programADD_func,name='program_add_page'),
    path('Admin_Resourse/', views.createadmin_resource,name='adminresource_form'),
    path('Admin_User/', views.createadmin_user,name='adminuser_form'),
    path('Admin_Resource_Update/<str:pk>/',views.resourceUpdate, name='adminresourceUpdate'),
    path('Admin_Resource_Delete/<str:pk>/',views.resourceDelete,name='adminresourceDelete'),
    path('Admin_User_Update/<str:pk>/',views.userUpdate, name='adminuserUpdate'),
    path('Admin_User_Delete/<str:pk>/',views.userDelete,name='adminuserDelete'),
    path('ContractorTracker/', views.contractorTracker_view,name='contract_tracker_page'),
    path('ContractorTracker_ADD/',views.contractorADD,name='contract_tracker_form'),
    path('Contractor_Delete/<str:pk>/',views.contractorDelete,name='contractorDelete'),
    path('Export_csv/',views.export,name='export_csv'),
]