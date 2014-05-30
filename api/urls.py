from django.conf.urls import patterns, include, url
import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'inventory', views.GetInventoryApiView)
router.register(r'pharmacy', views.PharmacyApiView)
urlpatterns = patterns(
    '',
    url(r'^drug/$', views.DrugListApiView.as_view(), name='drug_api'),
    url(r'^', include(router.urls)),
)
