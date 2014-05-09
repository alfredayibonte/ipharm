from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns(
    '',
    (r'^dashboard/$', views.Profile.as_view(), ),
)
