from .models import *
from django.shortcuts import get_object_or_404, render

def pocetna(req):
    letovi = Let.objects.all()
    gradovi = Grad.objects.all()
    return render(req,'letovi.html',{'letovi':letovi,'gradovi':gradovi})

def pretraga(req):
    iz = req.GET.get('od')
    dest = req.GET.get('do')
    letovi = Let.objects.filter(od__naziv=iz,do__naziv=dest)
    return render(req,'letovi.html',{'letovi':letovi})

def kupovna(req):
    if req.method == 'POST':
        print(4)
    else:
        flug = get_object_or_404(Let, id=req.GET.get('id'))
        ostalo = PreostaloKarata.objects.filter(let=flug).order_by('cena')
    return render(req,'kupovna.html',{'ostalo':ostalo,'let':flug})

