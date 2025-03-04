from django.contrib import admin
from .models import *

class GradAdmin(admin.ModelAdmin):
    list_display=('naziv','aerodrom','drzava')
class LetAdmin(admin.ModelAdmin):
    list_display=('od','do','vreme')

# Register your models here.
admin.site.register(Grad, GradAdmin)
admin.site.register(Let, LetAdmin)
