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
    
    # category = forms.ModelMultipleChoiceField(queryset=Categorys.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    # name = models.CharField(max_length=255, required=True)

    # name.widget.attrs.update


# user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.ManyToManyField(Categorys)
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(upload_to='static/image_post', blank=True)
#     added = models.DateField(auto_now_add=True)
#     update = models.DateField(auto_now=True)
