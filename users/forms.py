from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Обязательное поле.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')