from django.urls import path
from . import views

urlpatterns = [
    path('member_faculty_list', views.member_faculty_list, name='member_faculty_list'),
    path('member_faculty_list/<int:user_id>/', views.member_faculty_list, name='member_faculty_list'),
    path('admin_faculty_list/', views.admin_faculty_list, name='admin_faculty_list'),
    path('admin_faculty_list/<int:user_id>/', views.admin_faculty_list, name='admin_faculty_list'),
    path('superadmin_faculty_list/', views.superadmin_faculty_list, name='superadmin_faculty_list'),
    path('superadmin_faculty_list/<int:group_id>/', views.superadmin_faculty_list, name='superadmin_faculty_list'),
    path('superadmin_faculty_list/<int:group_id>/<int:user_id>/', views.superadmin_faculty_list, name='superadmin_faculty_list'),
    path('IPCR_Remarks_Create/<int:user_id>/', views.IPCR_Remarks_Create, name='IPCR_Remarks_Create'),
    path('IPCR_Approval/<int:user_id>/', views.IPCR_Approval, name='IPCR_Approval')
]
