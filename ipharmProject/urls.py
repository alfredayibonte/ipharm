from django.conf.urls import patterns, include, url
from django.contrib import admin
from ipharmProject import settings
import views
from inventories import views as drug
from pharmacies import views as pharmacy
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/(?P<username>\w+)/$', pharmacy.LocationSearch.as_view(), name='location_map'),
    url(r'^inventory/', include('inventories.urls', namespace='inventories')),
    url(r'^pharmacy/', include('pharmacies.urls', namespace='pharmacies')),
    url(r'^upload/', drug.UploadFile.as_view(), name='upload'),
    url(r'^api/',  include('api.urls', namespace='d')),
    url(r'login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'register/$', pharmacy.Register.as_view(), name='register'),
    url(r'logout/$', pharmacy.Logout.as_view(), name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'registration/password.html', 'post_change_redirect': 'pharmacies:pharmacy'}, name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
