from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=12, min_length=6, required=True, help_text='Required. 6-12 characters. Letters and digits only.')
    password1 = forms.CharField(min_length=6, required=True, help_text='Required. Minimum 6 characters. Can contain letters, digits and special characters.')
    password2 = forms.CharField(required=True, help_text='Required. Enter the same password as before, for verification.')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isalnum():
            raise forms.ValidationError('Username must be alphanumeric')
        return username
