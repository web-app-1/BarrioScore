from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Resena
from .forms import ResenaForm
from .forms import ResidencialForm
from .forms import PromotorForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después de registrarse
            return redirect('resenas')  # Redirigir a la lista de reseñas
    else:
        form = UserCreationForm()

    return render(request, 'registro/registrarse.html', {'form': form})

def inicio(request):
    # Obtener las reseñas más recientes
    resenas = Resena.objects.order_by('-fecha_publicacion')[:20]
    return render(request, 'inicio.html', {'resenas': resenas})


def pagina_inicio(request):
    # Obtener las últimas 20 reseñas ordenadas por fecha de publicación
    ultimas_resenas = Resena.objects.order_by('-fecha_publicacion')[:20]
    return render(request, 'inicio.html', {'resenas': ultimas_resenas})

def listar_resenas(request):
    # Obtener todas las reseñas ordenadas por fecha de publicación
    todas_resenas = Resena.objects.all().order_by('-fecha_publicacion')
    return render(request, 'resenas/listar_resenas.html', {'resenas': todas_resenas})


def buscar_resenas(request):
    residencial = request.GET.get('residencial')  # Obtiene el nombre del residencial desde el formulario de búsqueda
    resenas = Resena.objects.filter(residencial__nombre__icontains=residencial) if residencial else Resena.objects.all()
    return render(request, 'resenas/buscar_resenas.html', {'resenas': resenas, 'residencial': residencial})


@login_required
def agregar_resena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.usuario = request.user  # Asigna el usuario actual a la reseña
            resena.save()
            return redirect('resenas')  # Redirige a la lista de reseñas después de crearla
    else:
        form = ResenaForm()
    return render(request, 'resenas/agregar_resena.html', {'form': form})

@login_required
def agregar_residencial(request):
    if request.method == 'POST':
        form = ResidencialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # O redirigir a la página que prefieras
    else:
        form = ResidencialForm()
    return render(request, 'admin/agregar_residencial.html', {'form': form})


@staff_member_required  # Solo accesible para administradores
def agregar_promotor(request):
    if request.method == 'POST':
        form = PromotorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirige al panel de administración después de agregar el promotor
    else:
        form = PromotorForm()
    
    return render(request, 'admin/agregar_promotor.html', {'form': form})


@staff_member_required
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')