from django.test import TestCase
from .forms import ProductoForm
from django.urls import reverse
# Create your tests here.

class PruebasValidacionProducto(TestCase):
    def test_cantidad_minima(self):
        datos = {
            'nombre': 'Producto minimo',
            'cantidad': 1,
            'correo_contacto': 'prueba@ejemplo.com'
        }
        formulario = ProductoForm(data=datos)
        self.assertTrue(formulario.is_valid())

    def test_cantidad_maxima(self):
        datos = {
            'nombre': 'Producto maximo',
            'cantidad': 50,
            'correo_contacto': 'prueba@ejemplo.com'
        }
        formulario = ProductoForm(data=datos)
        self.assertTrue(formulario.is_valid())

    def test_cantidad_superior(self):
        datos = {
            'nombre': 'Producto invalido',
            'cantidad': 51,
            'correo_contacto': 'prueba@ejemplo.com'
        }
        formulario = ProductoForm(data=datos)
        self.assertFalse(formulario.is_valid())
        self.assertIn('cantidad', formulario.errors)

    def test_correo_valido(self):
        datos = {
            'nombre': 'Producto valido',
            'cantidad': 10,
            'correo_contacto': 'contacto@ejemplo.com'
        }
        formulario = ProductoForm(data=datos)
        self.assertTrue(formulario.is_valid())

    def test_correo_invalido(self):
        datos = {
            'nombre': 'Producto invalido',
            'cantidad': 10,
            'correo_contacto': 'correo-invalido'
        }
        formulario = ProductoForm(data=datos)
        self.assertFalse(formulario.is_valid())
        self.assertIn('correo_contacto', formulario.errors)

    def test_correo_vacio(self):
        datos = {
            'nombre': 'Producto sin correo',
            'cantidad': 10,
            'correo_contacto': ''
        }
        formulario = ProductoForm(data=datos)
        self.assertFalse(formulario.is_valid())
        self.assertIn('correo_contacto', formulario.errors)

    def test_correo_demasiado_largo(self):
        correo_largo = ('a' * 100) + '@ejemplo.com'
        datos = {
            'nombre': 'Producto correo largo',
            'cantidad': 10,
            'correo_contacto': correo_largo
        }
        formulario = ProductoForm(data=datos)
        self.assertFalse(formulario.is_valid())
        self.assertIn('correo_contacto', formulario.errors)

class PruebasAcceso(TestCase):
    def test_crear_requiere_autenticacion(self):
        url = reverse('crear_producto')
        respuesta = self.client.get(url, secure=True)
        self.assertEqual(respuesta.status_code, 302)
        self.assertIn('/login/', respuesta.url)

    def test_listar_es_publico(self):
        url = reverse('listar_productos')
        respuesta = self.client.get(url, secure=True)
        self.assertEqual(respuesta.status_code, 200)

    def test_listar_rechaza_post(self):
        respuesta = self.client.post(
            reverse('listar_productos'),
            secure=True
        )
        self.assertEqual(respuesta.status_code, 405)
        self.assertEqual(respuesta.headers.get('Allow'), 'GET')