from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url(r'^search/$', views.search, name='search'),
)
