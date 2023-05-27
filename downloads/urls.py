from django.urls import path
from . import views



urlpatterns = [
    path('download', views.download, name='download'),
    path('Show_IPCR', views.Show_IPCR, name = 'Show_IPCR'),
]
