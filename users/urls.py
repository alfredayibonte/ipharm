from django.conf.urls import patterns, url
from users import views
from django.contrib.auth import views as auth_views


urlpatterns = patterns(
    '',

    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'index.html'}, name='logout'),


)
