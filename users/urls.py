from django.conf.urls import patterns, url
from users import views
from django.contrib.auth import views as auth_views


urlpatterns = patterns(
    '',
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'index.html'}, name='logout'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^edit/$', views.edit_profile, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^people/$', views.people, name='people'),
    url(r'^another/(?P<username>\w+)/$', views.another, name='another'),
    url(r'^(?P<username>\w+)/$', views.Profile.as_view(), name='profile'),



)
