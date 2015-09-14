import os, sys
sys.path.append('/home/jindiying/env/onewait200/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'onewait200.settings'

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
