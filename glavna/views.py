from glavna.form import *
from .models import *
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
    error_message = None 
    if request.method == "POST":  
        username = request.POST.get("username")  
        password = request.POST.get("password")  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'  
            return redirect(next_url) 
        else:
            error_message = "Invalid credentials"  
    return render(request, 'accounts/login.html', {'error': error_message})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def pocetna(req):
    letovi = Let.objects.all()
    gradovi = Grad.objects.all()
    return render(req,'letovi.html',{'letovi':letovi,'gradovi':gradovi})

def pretraga(req):
    iz = req.GET.get('od')
    dest = req.GET.get('do')
    letovi = Let.objects.filter(od__naziv=iz,do__naziv=dest)
    return render(req,'letovi.html',{'letovi':letovi})

@login_required
def kupovna(req):
    if req.method == 'POST':
        forma = Kauform(req.POST)
        if forma.is_valid():
            tipkarte = req.POST.get('tip_karte')
            kolicina = int(req.POST.get('broj_karata'))
            izbor = get_object_or_404(PreostaloKarata, let=get_object_or_404(Let, id=req.GET.get('id')), tip_karte=tipkarte)
            if izbor.preostalo >= kolicina:
                izbor.preostalo -= kolicina
                izbor.save()
                for _ in range(kolicina):
                    KupljenaKarta.objects.create(
                        tip_karte=izbor.tip_karte,
                        kupac=req.user,
                        cena=izbor.cena,
                        let = get_object_or_404(Let, id=req.GET.get('id'))
                    )
                return redirect('uspesna_kupovina')
            else:
                return redirect('greska')
    else:
        flug = get_object_or_404(Let, id=req.GET.get('id'))
        ostalo = PreostaloKarata.objects.filter(let=flug).order_by('cena')
        forma = Kauform()
    return render(req,'kupovna.html',{'ostalo':ostalo,'let':flug,'forma':forma})

def uspesna_kupovina(zahtev):
    return render(zahtev,'uspesna-kupovina.html')

def greska(zahtev):
    return render(zahtev,'greskapage.html')

def kupljene_karte(zahtev):
    if zahtev.method == "POST":
        kupljene = KupljenaKarta.objects.filter(kupac=zahtev.user)
        return render(zahtev,'kupljene.html',{'kupljene':kupljene})
