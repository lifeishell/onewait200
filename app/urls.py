from django.conf.urls.defaults import *
from onewait200.app.views import get_relations

urlpatterns += patterns('',
    ('^get_relations/',  get_relations),
)