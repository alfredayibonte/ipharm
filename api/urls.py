from django.conf.urls import patterns, include, url
import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'inventories', views.InventoryApiView)
router.register(r'drugs', views.DrugApiView)
router.register(r'pharmacies', views.PharmacyApiView)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^find/', views.FindPharmacyView.as_view()),
)
