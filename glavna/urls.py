from django.urls import path
from . import views

urlpatterns = [
    path('', views.pocetna, name='home'),
    path('pretraga/', views.pretraga, name='rezpretrage'),
    path('kupovna/',views.kupovna, name='kupovna'),
    path('uspesna-kupovina',views.uspesna_kupovina, name='uspesna_kupovina'),
    path('greska', views.greska, name='greska'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('kupljene', views.kupljene_karte, name='kupljene'),
    ]