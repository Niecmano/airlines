from django.urls import path
from . import views

urlpatterns = [
    path('', views.pocetna),
    path('pretraga/', views.pretraga, name='rezpretrage'),
    ]