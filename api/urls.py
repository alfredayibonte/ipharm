from django.conf.urls import patterns, include, url
import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'inventory', views.InventoryApiView)
router.register(r'drug', views.DrugApiView)
router.register(r'pharmacy', views.PharmacyApiView)
urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
