import os
import sys
import sae
from application import wsgi

app_root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(app_root, 'virtualenv.bundle.zip'))

application = sae.create_wsgi_app(wsgi.application)
