from django.conf.urls import patterns, include, url
from django.contrib import admin
from guests.views import LoginFormView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mywed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', LoginFormView.as_view(), name='login'),
)