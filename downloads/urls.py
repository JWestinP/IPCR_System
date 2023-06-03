from django.urls import path
from . import views



urlpatterns = [
    path('download', views.download, name='download'),
    path('firstmidsem_ViewIPCR', views.firstmidsem_ViewIPCR, name = 'firstmidsem_ViewIPCR'),
    path('firstfinalsem_ViewIPCR', views.firstfinalsem_ViewIPCR, name = 'firstfinalsem_ViewIPCR'),
    path('secondmidsem_ViewIPCR', views.secondmidsem_ViewIPCR, name = 'secondmidsem_ViewIPCR'),
    path('secondfinalsem_ViewIPCR', views.secondfinalsem_ViewIPCR, name = 'secondfinalsem_ViewIPCR'),
    path('firstmidsem_download_pdf', views.firstmidsem_download_pdf, name = 'firstmidsem_download_pdf'),
    path('firstfinalsem_download_pdf', views.firstfinalsem_download_pdf, name = 'firstfinalsem_download_pdf'),
    path('secondmidsem_download_pdf', views.secondmidsem_download_pdf, name = 'secondmidsem_download_pdf'),
    path('secondfinalsem_download_pdf', views.secondfinalsem_download_pdf, name = 'secondfinalsem_download_pdf'),
    path('last_firstmidsem_ViewIPCR', views.last_firstmidsem_ViewIPCR, name = 'last_firstmidsem_ViewIPCR'),
    path('last_firstfinalsem_ViewIPCR', views.last_firstfinalsem_ViewIPCR, name = 'last_firstfinalsem_ViewIPCR'),
    path('last_secondmidsem_ViewIPCR', views.last_secondmidsem_ViewIPCR, name = 'last_secondmidsem_ViewIPCR'),
    path('last_secondfinalsem_ViewIPCR', views.last_secondfinalsem_ViewIPCR, name = 'last_secondfinalsem_ViewIPCR'),
    path('last_firstmidsem_download_pdf', views.last_firstmidsem_download_pdf, name = 'last_firstmidsem_download_pdf'),
    path('last_firstfinalsem_download_pdf', views.last_firstfinalsem_download_pdf, name = 'last_firstfinalsem_download_pdf'),
    path('last_secondmidsem_download_pdf', views.last_secondmidsem_download_pdf, name = 'last_secondmidsem_download_pdf'),
    path('last_secondfinalsem_download_pdf', views.last_secondfinalsem_download_pdf, name = 'last_secondfinalsem_download_pdf'),
    path('last_last_firstmidsem_ViewIPCR', views.last_last_firstmidsem_ViewIPCR, name = 'last_last_firstmidsem_ViewIPCR'),
    path('last_last_firstfinalsem_ViewIPCR', views.last_last_firstfinalsem_ViewIPCR, name = 'last_last_firstfinalsem_ViewIPCR'),
    path('last_last_secondmidsem_ViewIPCR', views.last_last_secondmidsem_ViewIPCR, name = 'last_last_secondmidsem_ViewIPCR'),
    path('last_last_secondfinalsem_ViewIPCR', views.last_last_secondfinalsem_ViewIPCR, name = 'last_last_secondfinalsem_ViewIPCR'),
    path('last_last_firstmidsem_download_pdf', views.last_last_firstmidsem_download_pdf, name = 'last_last_firstmidsem_download_pdf'),
    path('last_last_firstfinalsem_download_pdf', views.last_last_firstfinalsem_download_pdf, name = 'last_last_firstfinalsem_download_pdf'),
    path('last_last_secondmidsem_download_pdf', views.last_last_secondmidsem_download_pdf, name = 'last_last_secondmidsem_download_pdf'),
    path('last_last_secondfinalsem_download_pdf', views.last_last_secondfinalsem_download_pdf, name = 'last_last_secondfinalsem_download_pdf'),
    
]
