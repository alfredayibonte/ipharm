from django.conf.urls import patterns, url
import views as pharmacy

urlpatterns = patterns(
    '',
    url(r'^main/$', pharmacy.Main.as_view(), name='main'),
    url(r'^email/$', pharmacy.Email.as_view(), name='email'),
)
