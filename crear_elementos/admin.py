from django.contrib import admin
from crear_elementos.models import logins, identificacion

# Register your models here.

@admin.register(logins)
class login_admin(admin.ModelAdmin):
    list_display=['usuario', 'email', 'nombreLogin', 'url']

@admin.register(identificacion)
class identificacion_admin(admin.ModelAdmin):
    list_display=['nombreIdentificacion', 'nombreCompleto', 'numero']