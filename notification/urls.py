from django.urls import path
from . import views

urlpatterns = [
    path('member_notification', views.member_notification, name='member_notification'),
    path('admin_superadmin_notification', views.admin_superadmin_notification, name='admin_superadmin_notification'),
    path('create_notification', views.create_notification, name='create_notification'),
]