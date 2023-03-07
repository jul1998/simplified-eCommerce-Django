from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', "email", 'password1', 'password2')

    username = forms.CharField(label="Username", max_length=64,
                               widget=forms.TextInput(attrs={'placeholder': 'Your username',
                                                             'class': 'form-control'}))
    email = forms.CharField(label="Email", max_length=64,
                            widget=forms.TextInput(attrs={'placeholder': 'Your email',
                                                          'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=64,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Your password',
                                                                  'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", max_length=64,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password',
                                                                  'class': 'form-control'}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=64,
                               widget=forms.TextInput(attrs={'placeholder': 'Your username',
                                                             'class': 'form-control'}))
    password = forms.CharField(label="Password", max_length=64,
                              widget=forms.PasswordInput(attrs={'placeholder': 'Your password',
                                                                'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password'].label = "Password"

