from .models import *
from django.shortcuts import render

def pocetna(req):
    letovi = Let.objects.all()
    gradovi = Grad.objects.all()
    return render(req,'letovi.html',{'letovi':letovi,'gradovi':gradovi})

# def pretraga(req):
#     iz = req.GET.get('od')
#     dest = req.GET.get('do')
#     letovi = Let.objects.filter(od__naziv=iz,do__naziv=dest)
#     return render(req,'letovi.html',{'letovi':letovi})

def pretraga(req):
    iz = req.GET.get('od')
    dest = req.GET.get('do')

    print(f"Polaziste iz forme: {iz}")
    print(f"Destinacija iz forme: {dest}")

    letovi = Let.objects.filter(od__naziv=iz, do__naziv=dest)

    print(f"SQL Upit: {letovi.query}")  # Prikazuje SQL koji Django generiše

    return render(req, 'letovi.html', {'letovi': letovi})

