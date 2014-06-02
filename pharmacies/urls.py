from django.conf.urls import patterns, url
import views as pharmacy

urlpatterns = patterns(
    '',
    url(r'^main/$', pharmacy.Main.as_view(), name='main'),
    url(r'^email/$', pharmacy.Email.as_view(), name='email'),
    url(r'^sms/$', pharmacy.SMS.as_view(), name='sms'),
    url(r'^contact/$', pharmacy.Contact.as_view(), name='contact'),
    url(r'^delete_contact/$', pharmacy.DeleteContact.as_view(), name='delete_contact'),
    url(r'^contact_list/$', pharmacy.ContactList.as_view(), name='contact_list'),
    url(r'^edit_contact/$', pharmacy.EditContact.as_view(), name='edit_contact'),
    url(r'^user/$', pharmacy.PharmacyProfile.as_view(), name='pharmacy'),
    url(r'^add_user/$', pharmacy.AddUser.as_view(), name='add_user'),
    url(r'^delete_user/$', pharmacy.DeleteUser.as_view(), name='delete_user'),
    url(r'^edit_user/$', pharmacy.EditUser.as_view(), name='edit_user'),
    url(r'^map/$', pharmacy.Map.as_view(), name='map'),
    url(r'^change/$', pharmacy.ChangePassword.as_view(), name='change'),
)
