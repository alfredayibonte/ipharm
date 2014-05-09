from django.conf.urls import patterns, include, url

from views import login
urlpatterns = patterns(
    '',
    url(r'^login/', login, name='login' ),


)
