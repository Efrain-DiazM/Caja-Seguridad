from django.contrib import admin
from crear_clave_favorita.models import claveFavorita

# Register your models here.

@admin.register(claveFavorita)
class claveFavorita_admin(admin.ModelAdmin):
    list_display = ['nombreClave', 'pista']