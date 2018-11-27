"""
WSGI config for sam project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sam.settings")

application = get_wsgi_application()

"""
from django.core.wsgi import get_wsgi_application 
 
sys.path.append('/var/www/django_projects/sam_prod') 
# adjust the Python version in the line below as needed 
sys.path.append('/var/www/django_projects/lib/python2.7/site-packages') 
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sam.settings") 
 
try: 
    application = get_wsgi_application() 
except Exception: 
    # Error loading applications 
    if 'mod_wsgi' in sys.modules: 
        traceback.print_exc() 
        os.kill(os.getpid(), signal.SIGINT) 
        time.sleep(2.5) 
"""