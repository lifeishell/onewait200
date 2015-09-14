from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^get_relations/$', 'onewait200.app.views.get_relations', name='home'),
    url(r'^add_relation/$', 'onewait200.app.views.add_relation', name='relation'),
    url(r'^add_person/$', 'onewait200.app.views.add_person', name='person'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
