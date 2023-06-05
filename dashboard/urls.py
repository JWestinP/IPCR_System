from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard_admin_superadmin', views.dashboard_admin_superadmin , name='dashboard_admin_superadmin'),
]