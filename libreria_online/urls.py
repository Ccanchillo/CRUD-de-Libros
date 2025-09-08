"""
URLconf para el proyecto libreria_online.

La función `urlpatterns` lista las rutas URL a las vistas. Para más información, consulta:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Ejemplos:
Vista de función
    1. Agrega una importación:  from my_app import views
    2. Agrega una URL a urlpatterns:  path('', views.home, name='home')
Vista basada en clase
    1. Agrega una importación:  from other_app.views import Home
    2. Agrega una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otro URLconf
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),
]

# Servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
