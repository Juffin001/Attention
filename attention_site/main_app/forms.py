from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Target

class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label="Nick or Email", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User 
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Nick or Email", widget=forms.TextInput(attrs={'class': "form-input"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': "form-input"}))

class AddTargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['text', 'time_to_beat', 'day_to_beat', 'is_great', 'is_repeat', 'repeat_every']
