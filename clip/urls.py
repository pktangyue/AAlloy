from django.conf.urls import patterns, url
from clip import views

urlpatterns = patterns ('',
        url(r'^$', views.index, name = 'index' ),
        url(r'^submit/$', views.submit, name = 'submit' ),
        url(r'^recent/$', views.recent, name = 'recent' ),
        url(r'^history/$', views.history, name = 'history' ),
        url(r'^record/(?P<record_id>\d+)/$', views.record, name = 'record' ),
        )
