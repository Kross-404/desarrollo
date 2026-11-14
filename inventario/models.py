from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)]
    )
    correo_contacto = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre