from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from shockwave.settings import rel
admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$', 'frontend.views.main'),
    # url(r'^$', 'shockwave.views.home', name='home'),
    # url(r'^shockwave/', include('shockwave.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': rel('media')}),
)
