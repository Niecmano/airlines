from django.db import models

class Grad(models.Model):
    naziv = models.CharField(max_length=40)
    aerodrom = models.CharField(max_length=60)
    drzava = models.CharField(max_length=30)

    def __str__(self):
        return self.naziv

class Let(models.Model):
    od = models.ForeignKey(Grad,on_delete=models.RESTRICT, related_name="od")
    do = models.ForeignKey(Grad,on_delete=models.RESTRICT, related_name="do")
    vreme = models.DateTimeField()

    def __str__(self):
        return f'{self.od}-{self.do} {self.vreme.strftime('%d.%B %Y')}'
class TipKarte(models.Model):
    naziv = models.CharField(max_length=30)
    prtljag = models.CharField(max_length=100, default='ranac')
    dodusl = models.CharField(max_length=100, default='/')
    def __str__(self):
        return self.naziv

class PreostaloKarata(models.Model):
    let = models.ForeignKey(Let,on_delete=models.RESTRICT)
    tip_karte = models.ForeignKey(TipKarte, on_delete=models.RESTRICT)
    preostalo = models.PositiveIntegerField()
    cena = models.DecimalField(max_digits=7, decimal_places=2, default=5000.00)
    
