from django.urls import path
from . import views

urlpatterns = [
    path('member_notification', views.member_notification, name='member_notification'),
    path('admin_notification', views.admin_notification, name='admin_notification'),
]