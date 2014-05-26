from django.conf.urls import patterns, url
import views as pharmacy

urlpatterns = patterns(
    '',
    url(r'^main/$', pharmacy.Main.as_view(), name='main'),
    url(r'^email/$', pharmacy.Email.as_view(), name='email'),
    url(r'^sms/$', pharmacy.SMS.as_view(), name='sms'),
    url(r'^contact/$', pharmacy.Contact.as_view(), name='contact'),
    url(r'^edit/$', pharmacy.EditProfile.as_view(), name='edit'),
    url(r'^profile/$', pharmacy.Profile.as_view(), name='profile'),
    url(r'^user/$', pharmacy.PharmacyProfile.as_view(), name='pharmacy'),
    url(r'^map/$', pharmacy.MAP.as_view(), name='map'),
)
