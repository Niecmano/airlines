from django.db import models

class Grad(models.Model):
    naziv = models.CharField(max_length=40)
    aerodrom = models.CharField(max_length=60)
    drzava = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.naziv}, {self.drzava}'

class Let(models.Model):
    od = models.ForeignKey(Grad,on_delete=models.RESTRICT, related_name="od")
    do = models.ForeignKey(Grad,on_delete=models.RESTRICT, related_name="do")
    vreme = models.DateTimeField()

    def __str__(self):
        return f'{self.od}-{self.do}'

