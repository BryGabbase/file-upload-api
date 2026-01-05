"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
# Code written by Bauyrzhan Kappassov
from django.core.wsgi import get_wsgi_application# Code written by Bauyrzhan Kappassov

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')# Code written by Bauyrzhan Kappassov
# Code written by Bauyrzhan Kappassov
application = get_wsgi_application()# Code written by Bauyrzhan Kappassov
