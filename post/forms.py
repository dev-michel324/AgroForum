from django import forms
from django.db import models
from django.db.models import fields, query
from django.forms import widgets
from django.forms.fields import CharField

from .models import Comment, Post
from . models import Categorys
# from .models import CHOICES

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'image', 'description', 'category']
        error_messages = {
            'name': {
                'max_length': ('invalid number of characters.'),
            },
        }

class PostComment(forms.Form):
    comment = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(),
        )