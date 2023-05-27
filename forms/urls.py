from django.urls import path
from . import views

urlpatterns = [
    path('IPCR_Form', views.IPCR_Form, name = 'IPCR_Form'),
    path('IPCR_Form_Submit', views.IPCR_Form_Submit, name = 'IPCR_Form_Submit'),
    path('IPCR_Form_Already_Submitted', views.IPCR_Form_Already_Submitted, name = 'IPCR_Form_Already_Submitted'),
]
