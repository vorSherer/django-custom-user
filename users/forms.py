from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        models = CustomUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        models = CustomUser
        fields = ('email', 'username')

