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
    (r'^inventory/', include('inventories.urls', namespace='inventories')),
    (r'^pharmacy/', include('pharmacies.urls', namespace='pharmacies')),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

)
