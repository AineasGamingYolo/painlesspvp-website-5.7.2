import os, sys

# edit your username below
sys.path.append("/home/painless/public_html/painlesspvp.ml")

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'index.settings'

application = get_wsgi_application()