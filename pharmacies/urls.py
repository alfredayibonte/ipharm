from django.conf.urls import patterns, url
from pharmacies import views as pharmacy

urlpatterns = patterns(
    '',
    url(r'^main/$', pharmacy.Main.as_view(), name='main')
)
