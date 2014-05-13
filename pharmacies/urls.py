from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns(
    '',
    url(r'^main/$', views.Main.as_view(), name='main'),
    url(r'^email/$', views.Email.as_view(), name='email'),


)
