from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from ipharmProject import settings
import views
from inventories import views as drug
from pharmacies import views as pharmacy
from django.conf.urls.static import static
from pharmacies import serializers

router = routers.DefaultRouter()
router.register(r'users', serializers.UserViewSet)
router.register(r'groups', serializers.GroupViewSet)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^drug_list/$', drug.drug_list, name='drug_list'),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inventory/', include('inventories.urls', namespace='inventories')),
    url(r'^pharmacy/', include('pharmacies.urls', namespace='pharmacies')),
    url(r'^upload/', drug.UploadFile.as_view(), name='upload'),
    url(r'login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'register/$', pharmacy.Register.as_view(), name='register'),
    url(r'logout/$', pharmacy.Logout.as_view(), name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)