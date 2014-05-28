from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url(r'^drug/$', views.DrugListApiView.as_view(), name='drug_api'),
    url(r'^inventory/$', views.InventoryApiView.as_view(), name='inventory_api'),
    url('^pharmacy/$', views.PharmacyApiView.as_view(), name='pharmacy_api'),
)
