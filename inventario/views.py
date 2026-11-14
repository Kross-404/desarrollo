from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm


# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/listar.html', {
        'productos': productos
    })

@login_required
def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm()
    return render(request, 'inventario/formulario.html', {
        'formulario': formulario,
        'titulo': 'Registrar producto'
    })
@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm(instance=producto)
    return render(request, 'inventario/formulario.html', {
        'formulario': formulario,
        'titulo': 'Editar producto'
    })
@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'inventario/eliminar.html', {
        'producto': producto
    })