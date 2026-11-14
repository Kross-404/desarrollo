from django.contrib import admin
from .models import Producto

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'cantidad', 'correo_contacto')
    search_fields = ('nombre', 'correo_contacto')