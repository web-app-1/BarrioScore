from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Autenticación
    path('iniciar_sesion/', auth_views.LoginView.as_view(template_name='registro/iniciar_sesion.html'), name='iniciar_sesion'),
    path('cerrar_sesion/', auth_views.LogoutView.as_view(), name='cerrar_sesion'),
    path('registrarse/', views.registro, name='registrarse'),
    path('agregar-resena/', views.agregar_resena, name='agregar_resena'), # agregar resena
    path('agregar-residencial/', views.agregar_residencial, name='agregar_residencial'), # agregar residencial
    path('agregar-promotor/', views.agregar_promotor, name='agregar_promotor'), #agregar  promotor
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Listar y buscar reseñas
    path('resenas/', views.listar_resenas, name='resenas'),  # Mostrar todas las reseñas
    path('buscar-resenas/', views.buscar_resenas, name='buscar_resenas'),  # Buscar reseñas por residencial
    
    # Página de inicio
    path('', views.inicio, name='pagina_inicio'),  # Página de inicio con las reseñas más recientes
]
