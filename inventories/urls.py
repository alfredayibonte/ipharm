from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url(r'^add/$', views.AddDrug.as_view(), name='add'),
    url(r'^drug_list/$', views.Inventory.as_view(), name='drug_list'),
)
