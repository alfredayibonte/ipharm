from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url(r'^add/$', views.AddDrug.as_view(), name='add'),
    url(r'^drug_list/$', views.DrugList.as_view(), name='drug_list'),
    url(r'^inventory_list/$', views.InventoryList.as_view(), name='inventory_list')
)
