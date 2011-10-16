from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from shockwave.settings import rel

admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$', 'frontend.views.main'),
	url(r'^sample$', 'frontend.views.sample'),
	
	url(r'^info/(?P<term>.*)$', 'api.views.get_dataset_info'),
	url(r'^dataset/(?P<term>.*)$', 'api.views.get_dataset'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': rel('media')}),
)
