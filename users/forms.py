from django import forms
from django.contrib.auth import get_user_model
from users.models import Customer

User = get_user_model()


class MyRegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    username = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'username'})
    )

    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat'})
    )

    class Meta:
        model = Customer
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 == password2:
                return self.cleaned_data
        raise forms.ValidationError('Passwords do not match')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
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


    images = forms.ImageField(required=False)

    class Meta:
        model = Customer
        fields = ('username', 'first_name', 'last_name')
        exclude = ('password1', 'password2', 'email')

    def save(self, commit=True):
        user = super(EditUserForm, self).save(commit=False)
        user.images = self.cleaned_data['images']
        if commit:
            user.save()
        return user