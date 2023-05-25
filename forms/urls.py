from django.urls import path
from . import views

urlpatterns = [
    path('IPCR_Form', views.IPCR_Form, name = 'IPCR_Form'),
]
