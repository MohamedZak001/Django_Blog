from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile
from django import forms


class Reg(UserCreationForm):
    Email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username', 'Email', 'password1', 'password2',
        ]

class update_user(forms.ModelForm):
    Email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username', 'Email'
        ]

class update_profile(forms.ModelForm):
    class Meta:
        model = profile
        fields = [
            'image'
        ]