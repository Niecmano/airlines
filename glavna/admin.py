from django.contrib import admin
from .models import *

class GradAdmin(admin.ModelAdmin):
    list_display=('naziv','aerodrom','drzava')
class LetAdmin(admin.ModelAdmin):
    list_display=('od','do','vreme')
class PreostaloAdmin(admin.ModelAdmin):
    list_display=('let','tip_karte','preostalo','cena')

# Register your models here.
admin.site.register(Grad, GradAdmin)
admin.site.register(Let, LetAdmin)
admin.site.register(PreostaloKarata, PreostaloAdmin)
admin.site.register(TipKarte)
