from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls import patterns, include
from adminactions import actions
import adminactions.urls


admin.autodiscover()
actions.add_to_site(admin.site)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adminactions_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^demo/', include('demo.urls')),
    url(r'^adminactions/', include('adminactions.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
