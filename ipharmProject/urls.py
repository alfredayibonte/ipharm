from django.conf.urls import patterns, include, url

from django.contrib import admin
from ipharmProject import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^facebook/', include('django_facebook.urls'),),
    (r'^accounts/', include('django_facebook.auth_urls', namespace='accounts')),
    (r'^user/', include('users.urls', namespace='users')),
    (r'^pharmacy/', include('pharmacies.urls', namespace='pharmacies'))

)
