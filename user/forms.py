from django import forms as formModel
from django.contrib.auth import forms
from django.db import models
from django import forms as formdjango

from .models import User

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm):
        model = User
        fields = ('username', 'email')

class UserCreationForm(forms.UserCreationForm):
    email = formModel.EmailField(required=True, help_text='enter your email')
    photo = formdjango.ImageField(required=False, help_text='profile photo')

    class Meta(forms.UserCreationForm):
        model = User
        fields = ('username','photo', 'email', 'password1', 'password2', 'type')

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class PasswordChangeForm(forms.PasswordChangeForm):
    class Meta(forms.PasswordChangeForm):
        Model = User
        fields = ('old_password', 'new_password1', 'new_password2')