"""
Configuración WSGI para el proyecto libreria_online.

Expone el WSGI callable como una variable de nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulta
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libreria_online.settings')

application = get_wsgi_application()
