from django.contrib import admin
from crear_elementos.models import logins

# Register your models here.

@admin.register(logins)
class login_admin(admin.ModelAdmin):
    list_display=['usuario', 'email', 'nombreLogin', 'url']