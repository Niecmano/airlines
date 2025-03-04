from .models import *
from django.shortcuts import render

def pocetna(req):
    letovi = Let.objects.all()
    gradovi = Grad.objects.all()
    return render(req,'letovi.html',{'letovi':letovi,'gradovi':gradovi})
