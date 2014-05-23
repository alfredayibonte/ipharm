from django import forms
from django.contrib.auth import get_user_model
from pharmacies.models import Pharmacy, MyUser, Client

User = get_user_model()


class MyRegistrationForm(forms.ModelForm):
    email = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    username = forms.CharField(
        max_length=50,
        required=True,
    )
    pharmacy = forms.CharField(
        max_length=100,
        required=True,
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput()
    )
    repeat = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = MyUser
        fields = ('username', 'pharmacy', 'email', 'password', 'repeat')

    def clean_repeat(self):
        password1 = self.cleaned_data.get('repeat')
        password2 = self.cleaned_data.get('password')
        if password1 and password2:
            if password1 == password2:
                return self.cleaned_data
        raise forms.ValidationError('Passwords do not match')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Pharmacy.objects.create(user=user, name=self.cleaned_data['pharmacy'])
        return user


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ContactForm, self).__init__(*args, **kwargs)

    last_activity = forms.DateField(required=False)
    joined_date = forms.DateField(required=False)
    email = forms.EmailField(required=False)
    address = forms.CharField(required=False)
    telephone = forms.CharField(required=True)
    note = forms.CharField(required=False)
    name = forms.CharField(required=True)

    class Meta:
        model = Client
        fields = ('email', 'address', 'telephone', 'name', 'note', 'last_activity', 'date_joined')

    def save(self, commit=True):
        if commit:
            pharmacy = Pharmacy.objects.get(user=self.request.user)
            client = Client.objects.create(pharmacy=pharmacy,
                                           email=self.request.POST['email'],
                                           address=self.request.POST['address'],
                                           telephone=self.request.POST['telephone'],
                                           name=self.request.POST['name'],
                                           note=self.request.POST['note'],
                                           )
        return client


