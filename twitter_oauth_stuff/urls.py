from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from shockwave.settings import rel
from twitterauth.views import *
admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$', 'frontend.views.main'),
	url('^login/$', 'frontend.views.login'),
	url('^twitter/$', twitter_signin, name='login'),
    url('^return/$', twitter_return, name='return'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': rel('media')}),
)
