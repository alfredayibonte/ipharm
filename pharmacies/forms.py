from django import forms
from django.contrib.auth import get_user_model
from pharmacies.models import Pharmacy, MyUser

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


class EditUserForm(forms.ModelForm):
    location = forms.CharField(
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Location',
                   'class': 'input-huge'}
        )
    )
    username = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={'placeholder': 'username',
                   'class': 'input-huge'}
        )
    )
    first_name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={'placeholder': 'First Name',
                   'class': 'input-huge'}
        )
    )
    last_name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={'placeholder': 'Last Name',
                   'class': 'input-huge'}
        )
    )

    oneliner = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'One-liner',
                   'class': 'input-huge'}
        )
    )
    images = forms.ImageField(required=False)

    class Meta:
        model = Pharmacy
        fields = ('username', 'first_name', 'last_name', 'oneliner', 'location')
        exclude = ('password1', 'password2', 'email')

    def save(self, commit=True):
        user = super(EditUserForm, self).save(commit=False)
        user.images = self.cleaned_data['images']
        if commit:
            user.save()
        return user