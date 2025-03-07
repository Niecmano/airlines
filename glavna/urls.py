from django.urls import path
from . import views

urlpatterns = [
    path('', views.pocetna),
    path('pretraga/', views.pretraga, name='rezpretrage'),
    path('kupovna/',views.kupovna, name='kupovna')
    ]