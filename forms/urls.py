from django.urls import path
from . import views

urlpatterns = [
    path('IPCR_pg1', views.IPCR_pg1, name = 'IPCR_pg1'),
    path('IPCR_pg2', views.IPCR_pg2, name = 'IPCR_pg2'),
    path('IPCR_pg3', views.IPCR_pg3, name = 'IPCR_pg3'),
    path('IPCR_pg4', views.IPCR_pg4, name = 'IPCR_pg4'),
    path('IPCR_pg5', views.IPCR_pg5, name = 'IPCR_pg5'),
    path('IPCR_pg6', views.IPCR_pg6, name = 'IPCR_pg6'),
    path('IPCR_pg7', views.IPCR_pg7, name = 'IPCR_pg7'),
    path('IPCR_pg8', views.IPCR_pg8, name = 'IPCR_pg8'),
    path('Show_IPCR', views.Show_IPCR, name = 'Show_IPCR'),
]
