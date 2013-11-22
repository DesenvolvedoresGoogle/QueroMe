from django.conf.urls.defaults import *
from django.contrib import admin
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    url('^admin/', include(admin.site.urls)),

    url('^login/$', 'django.contrib.auth.views.login', name='login'),
    url('^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url('^register/$', 'core.views.register', name='register'),
)
