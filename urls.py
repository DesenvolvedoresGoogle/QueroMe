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
    url('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}, name='home'),
    url('^admin/', include(admin.site.urls)),

    url('^login/$', 'django.contrib.auth.views.login', name='login'),
    url('^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url('^register/$', 'core.views.register', name='register'),
    url('^wish/$', 'core.views.wish', name='wish'),
    url('^listar-desejos/$', 'core.views.listar_desejos', name='listar'),
    url('^system/show/$', 'core.views.show', name='show'),

    #URL`s do novo layout.
#    (r'^system/(.*)$', 'django.views.static.serve',
#     {'document_root': 'templates/system/','show_indexes':True}),
#    (r'^website/(.*)$', 'django.views.static.serve',
#     {'document_root': 'templates/website/','show_indexes':True}),

    url('^system/$', 'core.views.system_home', name='system_home'),
    url('^website/$', 'core.views.website_home', name='website_home'),
)
