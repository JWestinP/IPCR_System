from django.urls import path
from . import views

urlpatterns = [
    path('member_faculty_list', views.member_faculty_list, name='member_faculty_list'),
    path('admin_faculty_list/<str:username>/', views.admin_faculty_list, name='admin_faculty_list'),
]