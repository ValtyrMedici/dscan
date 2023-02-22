from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_dscan, name='dscan-home'),
    path('scan/dscan/', views.view_scan, name='dscan-scan'),
]