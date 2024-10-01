from django.urls import path, include
from django.contrib import admin
from SiteApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('SiteApp.urls')),
    path('', views.pagina_inicio, name='pagina_inicio'),  # Página de inicio
    path('listar-resenas/', views.listar_resenas, name='listar_resenas'),  # Nueva URL para listar reseñas
]
