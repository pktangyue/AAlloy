import sae
from application import wsgi

application = sae.create_wsgi_app(wsgi.application)
