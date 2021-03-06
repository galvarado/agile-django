from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_agile/', include('django_agile.foo.urls')),
    (r'^', include('agile.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (
        r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], # remove the slash at the begining
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True},
    ),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )